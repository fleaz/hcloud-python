# -*- coding: utf-8 -*-
from hcloud.core.domain import BaseDomain

from hcloud.helpers.descriptors import ISODateTime


class Server(BaseDomain):
    __slots__ = (
        "id",
        "name",
        "status",
        "public_net",
        "server_type",
        "datacenter",
        "image",
        "iso",
        "rescue_enabled",
        "locked",
        "backup_window",
        "outgoing_traffic",
        "ingoing_traffic",
        "included_traffic",
        "protection",
        "labels",
        "volumes",
    )

    created = ISODateTime()

    def __init__(
        self,
        id,
        name=None,
        status=None,
        created=None,
        public_net=None,
        server_type=None,
        datacenter=None,
        image=None,
        iso=None,
        rescue_enabled=None,
        locked=None,
        backup_window=None,
        outgoing_traffic=None,
        ingoing_traffic=None,
        included_traffic=None,
        protection=None,
        labels=None,
        volumes=None,
    ):
        self.id = id
        self.name = name
        self.status = status
        self.created = created
        self.public_net = public_net
        self.server_type = server_type
        self.datacenter = datacenter
        self.image = image
        self.iso = iso
        self.rescue_enabled = rescue_enabled
        self.locked = locked
        self.backup_window = backup_window
        self.outgoing_traffic = outgoing_traffic
        self.ingoing_traffic = ingoing_traffic
        self.included_traffic = included_traffic
        self.protection = protection
        self.labels = labels
        self.volumes = volumes


class CreateServerResponse(BaseDomain):
    __slots__ = (
        "server",
        "action",
        "next_actions",
        "root_password"
    )

    def __init__(
            self,
            server,          # type: BoundServer
            action,          # type: BoundAction
            next_actions,    # type: List[Action]
            root_password    # type: str
    ):
        self.server = server
        self.action = action
        self.next_actions = next_actions
        self.root_password = root_password


class ResetPasswordResponse(BaseDomain):
    __slots__ = (
        "action",
        "root_password"
    )

    def __init__(
            self,
            action,          # type: BoundAction
            root_password    # type: str
    ):
        self.action = action
        self.root_password = root_password


class EnableRescueResponse(BaseDomain):
    __slots__ = (
        "action",
        "root_password"
    )

    def __init__(
            self,
            action,          # type: BoundAction
            root_password    # type: str
    ):
        self.action = action
        self.root_password = root_password


class RequestConsoleResponse(BaseDomain):
    __slots__ = (
        "action",
        "wss_url",
        "password"
    )

    def __init__(
            self,
            action,     # type: BoundAction
            wss_url,    # type: str
            password,   # type: str
    ):
        self.action = action
        self.wss_url = wss_url
        self.password = password
