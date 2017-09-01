# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import falcon

from . import Resource


class ApiQuote(Resource):

    def on_get(self, req, resp):
        print(req.context['params'])

        req.context['result'] = None
        resp.status = falcon.HTTP_200
        resp.set_headers({})