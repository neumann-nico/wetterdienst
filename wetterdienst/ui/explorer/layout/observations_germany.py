# -*- coding: utf-8 -*-
# Copyright (c) 2018-2021, earthobservations developers.
# Distributed under the MIT License. See LICENSE for more info.
import operator

import dash_core_components as dcc
import dash_html_components as html
from dash.exceptions import PreventUpdate
from dash_bootstrap_components import Input
from dash_html_components import Output

from wetterdienst.api import ApiEndpoints
from wetterdienst.provider.dwd.observation import (
    DwdObservationDataset,
    DwdObservationPeriod,
    DwdObservationResolution,
)


def get_providers():
    return [
        {"label": provider, "value": provider} for provider in ApiEndpoints
    ]


def get_parameters():
    return sorted(
        [{"label": param.value, "value": param.value} for param in DwdObservationDataset],
        key=operator.itemgetter("label"),
    )


def get_resolutions():
    return [{"label": param.value, "value": param.value} for param in DwdObservationResolution]


def get_periods():
    return [{"label": param.value, "value": param.value} for param in DwdObservationPeriod]


def dashboard_layout() -> html:
    """
    Dashboard layout for observations in Germany.
    """
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Div("Provider:"),
                            dcc.Dropdown(
                                id="select-provider",
                                options=get_providers(),
                                value=None,
                                multi=False,
                                className="dcc_control",
                            ),
                            html.Div("Network:"),
                            dcc.Dropdown(
                                id="select-network",
                                # options=None,
                                value=None,
                                multi=False,
                                className="dcc_control",
                            ),
                            html.Div("Resolution:"),
                            dcc.Dropdown(
                                id="select-resolution",
                                # options=None,
                                value=None,
                                multi=False,
                                className="dcc_control",
                            ),
                            html.Div("Dataset:"),
                            dcc.Dropdown(
                                id="select-dataset",
                                # options=None,
                                value=None,
                                multi=False,
                                className="dcc_control",
                            ),
                            html.Div("Period:"),
                            dcc.Dropdown(
                                id="select-period",
                                options=get_periods(),
                                value=DwdObservationPeriod.RECENT.value,
                                multi=False,
                                className="dcc_control",
                            ),
                            html.Div("Station:"),
                            dcc.Dropdown(
                                id="select-station",
                                multi=False,
                                className="dcc_control",
                            ),
                            html.Div("Variable:"),
                            dcc.Loading(
                                id="loading-1",
                                children=[
                                    dcc.Dropdown(
                                        id="select-variable",
                                        multi=False,
                                        className="dcc_control",
                                    ),
                                    html.Div(
                                        [],
                                        id="dataframe-values",
                                        style={"display": "None"},
                                    ),
                                ],
                            ),
                        ],
                        id="navigation",
                        className="col wd-panel d-flex flex-column",
                    ),
                    html.Div(
                        [
                            html.Div(
                                id="status-response-stations",
                            ),
                            html.Hr(),
                            html.Div(
                                id="status-response-values",
                            ),
                        ],
                        id="status-response",
                        className="col wd-panel flex-column",
                    ),
                    html.Div(
                        [dcc.Graph(id="map-stations")],
                        id="map",
                        className="col wd-panel",
                    ),
                ],
                id="header",
                className="d-flex flex-row",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            dcc.Graph(id="graph-values"),
                        ],
                        id="graph",
                        className="col wd-panel",
                    ),
                ],
                className="d-flex flex-row",
            ),
            html.Div([], id="dataframe-stations", style={"display": "None"}),
        ],
    )


