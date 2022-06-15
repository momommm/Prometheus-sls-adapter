import logging
from flask import Flask, request, Response
from querys import parse_data, SlsQuery

from proto import remote_pb2
import snappy

app = Flask(__name__)
slsQ = SlsQuery(url='https://metric-bucket-overseas.ap-southeast-1.log.aliyuncs.com/prometheus/metric-bucket-overseas/infra_metrics_60d/')
logging.basicConfig(level=logging.INFO)


@app.route("/")
def index():
    return Response("<h1>403 Forbidden<h1/>", status=403)


@app.route("/read", methods=["POST"])
def read():
    msg = remote_pb2.ReadRequest()
    msg.ParseFromString(snappy.uncompress(request.data))

    slsQ.set_auth(request.authorization['username'], request.authorization['password'])
    if request.headers['X-Prometheus-Remote-Read-Version'] != '0.1.0':
        return Response("<h1> Protocol error <h1/>", status=404)
    query = msg.queries[0]
    metric_name = ''
    for matcher in query.matchers:
        if matcher.name == '__name__':
            metric_name = f'{matcher.value}'

    matchers = []
    for matcher in query.matchers:
        if matcher.name != '__name__':
            if matcher.type == 0:
                matchers.append(f'{matcher.name}="{matcher.value}"')
            elif matcher.type == 1:
                matchers.append(f'{matcher.name}!="{matcher.value}"')
            elif matcher.type == 2:
                matchers.append(f'{matcher.name}=~"{matcher.value}"')
            elif matcher.type == 3:
                matchers.append(f'{matcher.name}!~"{matcher.value}"')

    query_str = f'{metric_name}' + '{' + f'{",".join(matchers)}' + '}'
    if not matchers:
        query_str = metric_name
    app.logger.debug(f'query_str:  {query_str}')
    start_ms = query.hints.start_ms
    end_ms = query.hints.end_ms

    resp = Response()
    resp.headers['Content-Type'] = 'application/x-protobuf'
    resp.headers['Content-Encoding'] = 'snappy'

    read_response = remote_pb2.ReadResponse()

    if query.hints.range_ms:
        content = slsQ.sls_query_range(query_str=query_str, start_ms=start_ms, end_ms=end_ms,
                                       step_ms=query.hints.step_ms)
    else:
        content = slsQ.sls_query(query_str=query_str, start_ms=start_ms, end_ms=end_ms)

    if content['status'] == 'error':
        return Response(content['error'], status=500)

    parse_data(read_response=read_response, data=content['data'])
    resp.set_data(snappy.compress(read_response.SerializeToString()))

    return resp
