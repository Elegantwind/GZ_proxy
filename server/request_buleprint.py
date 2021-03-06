# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import json
from sanic import Sanic
from sanic.response import json as sanic_json, text as sanic_text
from sanic.blueprints import Blueprint
from DataBaseFunction.Real_time_data_statistics_SQL import select_realtime_all, delete_realtime_table
from DataBaseFunction.Filter_match import select_filter_all, insert_filter_data, select_id_delete_filter, \
    delete_filter_table, select_id_filter
from basefunction.config_function import config_writer, config_reader
from basefunction.create_filter_match import created_new_match

realtime = Blueprint('request')

selected_filter_path = './temp/Filter.yml'


@realtime.route('/show_all_request')
async def show_all_redirect(request):
    db_data = select_realtime_all()
    return sanic_json({'data': db_data})


@realtime.route('/clear_all_request')
async def clear_all_redirect(request):
    try:
        delete_realtime_table()
        code = 'ok'
    except:
        code = 'error'
    return sanic_json({'code': code})


@realtime.route('/show_all_filter')
async def show_all_filter(request):
    try:
        db_data = select_filter_all()
        code = 'ok'
    except:
        db_data = []
        code = 'error'
    return sanic_json({'data': db_data, 'code': code})


@realtime.route('/add_filter', methods=['POST'])
async def add_filter(request):
    match = request.form['match'][0]
    try:
        describe = request.form['describe'][0]
    except Exception as e:
        print(e)
        describe = ''
    insert_filter_data(match, describe)
    return sanic_json({"code": "ok"})


@realtime.route('/select_filter', methods=['POST'])
async def select_filter(request):
    delete_id = int(request.form['id'][0])
    try:
        select_filter = select_id_filter(delete_id)
        config_writer(select_filter, selected_filter_path)
        code = 'ok'
    except Exception as e:
        print(e)
        code = 'error'
    return sanic_json({"code": code})


@realtime.route('/using_filter')
async def using_filter(request):
    try:
        # data = config_reader(selected_filter_path)
        data = created_new_match()
        # print(str(data))
        code = 'ok'
    except Exception as e:
        print(e)
        code = 'error'
        data = None
    return sanic_json({"code": code, "data": str(data)})


@realtime.route('/delete_filter', methods=['POST'])
async def delete_filter(request):
    delete_id = int(request.form['id'][0])
    try:
        select_id_delete_filter(delete_id)
        code = 'ok'
    except Exception as e:
        print(e)
        code = 'error'
    return sanic_json({"code": code})


@realtime.route('/clear_filter')
async def clear_filter(request):
    try:
        delete_filter_table()
        code = 'ok'
    except Exception as e:
        print(e)
        code = 'error'
    return sanic_json({"code": code})


@realtime.route('/cancel_filter')
async def cancel_filter(request):
    try:
        data = config_writer(None, selected_filter_path)
        code = 'ok'
    except Exception as e:
        print(e)
        code = 'error'
    return sanic_json({"code": code})
