# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import falcon

from . import Resource


class ApiKinesisEvent(Resource):

    def on_get(self, req, resp):

        req.context['result'] = None
        resp.status = falcon.HTTP_200
        resp.set_headers({})

    def on_post(self, req, resp):

        req.context['result'] = None
        resp.status = falcon.HTTP_200
        resp.set_headers({})