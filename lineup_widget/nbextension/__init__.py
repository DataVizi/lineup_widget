#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Samuel Gratzl.
# Distributed under the terms of the MIT License.

def _jupyter_nbextension_paths():
  return [{
    'section': 'notebook',
    'src': 'nbextension/static',
    'dest': 'lineup_widget',
    'require': 'lineup_widget/extension'
  }]
