from common.constant import StatusCode
from common.utils import generate_lambda_response
from contract_api.config import NETWORK_ID
from contract_api.config import IPFS_URL
from contract_api.config import NETWORKS
from contract_api.consumers.mpe_event_consumer import MPEEventConsumer
from contract_api.consumers.organization_event_consumer import OrganizationEventConsumer
from contract_api.consumers.service_event_consumer import ServiceEventConsumer


def organization_event_consumer_handler(event, context):
    try:

        OrganizationEventConsumer(NETWORKS[NETWORK_ID]["ws_provider"],IPFS_URL['url'],IPFS_URL['port']).on_event(event)
        return generate_lambda_response(200,StatusCode.OK)
    except Exception as e:
        print(e)
        return generate_lambda_response(500,str(e))


def service_event_consumer_handler(event, context):
    try:
        ServiceEventConsumer(NETWORKS[NETWORK_ID]["ws_provider"],IPFS_URL['url'],IPFS_URL['port']).on_event(event)
        return generate_lambda_response(200, StatusCode.OK)
    except Exception as e:
        raise e
        return generate_lambda_response(500, str(e))


def mpe_event_consumer_handler(event,context):
    try:
        MPEEventConsumer(NETWORKS[NETWORK_ID]["ws_provider"]).on_event(event)
        return generate_lambda_response(200, StatusCode.OK)

    except Exception as e:
        print(e)
        return generate_lambda_response(500, str(e))