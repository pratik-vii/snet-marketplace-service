from cerberus import Validator

from common.logger import get_logger
from registry.constants import UserType

logger = get_logger(__name__)

SERVICE_METADATA_SCHEMA = {
    "version": {
        "type": "integer",
        "empty": False
    },
    "display_name": {
        "type": "string",
        "empty": False
    },
    "encoding": {
        "type": "string",
        "empty": False
    },
    "service_type": {
        "type": "string",
        "empty": False
    },
    "model_ipfs_hash": {
        "type": "string",
        "empty": False
    },
    "mpe_address": {
        "type": "string",
        "empty": False
    },
    "groups": {
        "type": "list",
        "schema": {
            "type": "dict",
            "schema": {
                "group_name": {
                    "type": "string",
                    "empty": False
                },
                "free_calls": {
                    "type": "integer",
                    "empty": False
                },
                "free_call_signer_address": {
                    "type": "string",
                    "empty": False
                },
                "daemon_addresses": {
                    "type": "list",
                    "schema": {
                        "type": "string",
                        "empty":True

                    }
                },
                "pricing": {
                    "type": "list",
                    "schema": {
                        "type": "dict",
                        "schema": {
                            "price_model": {
                                "type": "string"
                            },
                            "price_in_cogs": {
                                "type": "integer"
                            },
                            "default": {
                                "type": "boolean"
                            }
                        }
                    },
                },
                "endpoints": {
                    "type": "list",
                    "empty": False
                },
                "group_id": {
                    "type": "string",
                    "empty": False
                }
            }
        }
    },
    "service_description": {
        "type": "dict",
        "schema": {
            "url": {
                "type": "string"
            },
            "short_description": {
                "type": "string"
            },
            "description": {
                "type": "string"
            }
        }
    },
    "assets": {
        "type": "dict",
        "schema": {
            "hero_image": {
                "type": "string"
            }
        }
    },
    "contributors": {
        "type": "list"
    },
}
REQUIRED_ASSETS_FOR_METADATA = ['hero_image']


class Service:
    def __init__(self, org_uuid, uuid, service_id, display_name, short_description, description, project_url, proto,
                 assets, ranking, rating, contributors, tags, mpe_address, metadata_uri, groups, service_state):
        self._org_uuid = org_uuid
        self._uuid = uuid
        self._service_id = service_id
        self._display_name = display_name
        self._short_description = short_description
        self._description = description
        self._project_url = project_url
        self._proto = proto
        self._assets = assets
        self._ranking = ranking
        self._rating = rating
        self._contributors = contributors
        self._tags = tags
        self._mpe_address = mpe_address
        self._metadata_uri = metadata_uri
        self._groups = groups
        self._service_state = service_state
        self._comments = {UserType.SERVICE_PROVIDER.value: "", UserType.SERVICE_APPROVER.value: ""}

    def to_dict(self):
        return {
            "org_uuid": self._org_uuid,
            "service_uuid": self._uuid,
            "service_id": self._service_id,
            "display_name": self._display_name,
            "short_description": self._short_description,
            "description": self._description,
            "project_url": self._project_url,
            "proto": self._proto,
            "assets": self._assets,
            "ranking": self._ranking,
            "rating": self._rating,
            "contributors": self._contributors,
            "tags": self._tags,
            "mpe_address": self._mpe_address,
            "metadata_uri": self._metadata_uri,
            "groups": [group.to_dict() for group in self._groups],
            "service_state": self._service_state.to_dict(),
            "comments": self._comments
        }

    def to_metadata(self):
        return {
            "version": 1,
            "display_name": self._display_name,
            "encoding": self.proto.get("encoding", ""),
            "service_type": self.proto.get("service_type", ""),
            "model_ipfs_hash": self.proto.get("model_ipfs_hash", ""),
            "mpe_address": self._mpe_address,
            "groups": [group.to_metadata() for group in self._groups],
            "service_description": {
                "url": self._project_url,
                "short_description": self.short_description,
                "description": self._description
            },
            "assets": self.prepare_assets_for_metadata(),
            "contributors": self._contributors
        }

    @property
    def org_uuid(self):
        return self._org_uuid

    @property
    def uuid(self):
        return self._uuid

    @property
    def service_id(self):
        return self._service_id

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, val):
        self._display_name = val

    @property
    def short_description(self):
        return self._short_description

    @short_description.setter
    def short_description(self, val):
        self._short_description = val

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, val):
        self._description = val

    @property
    def project_url(self):
        return self._project_url

    @project_url.setter
    def project_url(self, val):
        self._project_url = val

    @property
    def proto(self):
        return self._proto

    @proto.setter
    def proto(self, proto):
        self._proto = proto

    @property
    def assets(self):
        return self._assets

    @assets.setter
    def assets(self, assets):
        self._assets = assets

    @property
    def ranking(self):
        return self._ranking

    @property
    def rating(self):
        return self._rating

    @property
    def contributors(self):
        return self._contributors

    @contributors.setter
    def contributors(self, val):
        self._contributors = val

    @property
    def metadata_uri(self):
        return self._metadata_uri

    @metadata_uri.setter
    def metadata_uri(self, metadata_uri):
        self._metadata_uri = metadata_uri

    @property
    def groups(self):
        return [group for group in self._groups]

    @groups.setter
    def groups(self, val):
        self._groups = val

    @property
    def service_state(self):
        return self._service_state

    @service_state.setter
    def service_state(self, service_state):
        self._service_state = service_state

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, val):
        self._tags = val

    @property
    def mpe_address(self):
        return self._mpe_address

    @mpe_address.setter
    def mpe_address(self, val):
        self._mpe_address = val

    @property
    def comments(self):
        return self._comments

    @comments.setter
    def comments(self, comments):
        self._comments[UserType.SERVICE_PROVIDER.value] = comments.get(UserType.SERVICE_PROVIDER.value, "")
        self._comments[UserType.SERVICE_APPROVER.value] = comments.get(UserType.SERVICE_APPROVER.value, "")

    @staticmethod
    def is_metadata_valid(service_metadata):
        logger.info(f"service_metadata: {service_metadata}")
        validator = Validator()
        is_valid = validator.validate(service_metadata, SERVICE_METADATA_SCHEMA)
        logger.info(validator.errors)
        return is_valid

    def is_major_change(self, other):
        return False

    def prepare_assets_for_metadata(self):
        metadata_assets = {}
        for asset in self.assets.keys():
            if asset in REQUIRED_ASSETS_FOR_METADATA:
                metadata_assets.update({asset: self.assets[asset].get("ipfs_hash", "")})
        return metadata_assets


