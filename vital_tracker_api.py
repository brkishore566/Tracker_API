from flask import Flask, request, jsonify
import pandas as pd
import numpy

app = Flask(__name__)

@app.route('/vitals_input', methods=['POST'])
def vitals_input():
     if request.method == 'POST':
         df = pd.read_csv('/Users/kishorer/flask/user_vitals.csv')
         data = request.get_json()
         # import pdb
         # pdb.set_trace()
         for record in data:
             vital = [record['user_id'], record['timestamp'], record['heart_rate'], record['respiration_rate'],
             record['activity']]
             df = df.append(pd.Series(vital, index=df.columns), ignore_index=True)
             df.to_csv('/Users/kishorer/flask/user_vitals.csv', index=False)

         return {'message': 'record created'}, 201

def find_avg(arr):
    return int(numpy.mean(arr))

def find_min(arr):
    return numpy.min(arr)

def find_max(arr):
    return numpy.max(arr)

def calc_records(df, i, time_frame):
    avg_hr = find_avg(df['heart_rate'][i:i + (time_frame * 60)])
    min_rr = find_min(df['respiration_rate'][i:i + (time_frame * 60)])
    max_hr = find_max(df['heart_rate'][i:i + (time_frame * 60)])
    avg_rr = find_avg(df['respiration_rate'][i:i + (time_frame * 60)])
    return avg_hr, min_rr, max_hr, avg_rr

@app.route('/vitals_output', methods=['GET'])
def vitals_output():

     if request.method == 'GET':
         response = []
         if (len(request.args) == 1 and 'time_frame' in request.args):
             time_frame = int(request.args['time_frame'])
             if time_frame <= 0 or time_frame > 60:
                 return {'message': 'time_frame should be greater than 0 minutes and less than 60 minutes'}, 400
             else:
                 for i in range(0, len(df), time_frame * 60):
                     seg_start = df['timestamp'][i]
                     if i + (time_frame * 60) < len(df):
                         seg_end = df['timestamp'][i + (time_frame * 60)]
                     else:
                         seg_end = df['timestamp'][len(df) - 1]
                     avg_hr, min_rr, max_hr, avg_rr = calc_records(df, i, time_frame)
                     response += [{'userid':'123', 'seg_start':seg_start, 'seg_end':seg_end, 'avg_hr':avg_hr,\
                        'min_rr':min_rr, 'max_hr':max_hr, 'avg_rr':avg_rr}]

                 return response, 200

         elif not request.args:
             df = pd.read_csv('/Users/kishorer/flask/user_vitals.csv')
             time_frame = 15
             for i in range(0, len(df), time_frame * 60):
                 seg_start = df['timestamp'][i]
                 if i + (time_frame * 60) < len(df):
                     seg_end = df['timestamp'][i + (time_frame * 60)]
                 else:
                     seg_end = df['timestamp'][len(df)-1]
                 avg_hr, min_rr, max_hr, avg_rr = calc_records(df, i, time_frame)
                 response += [{'userid': '123', 'seg_start': str(seg_start), 'seg_end': str(seg_end), 'avg_hr': str(avg_hr), \
                               'min_rr': str(min_rr), 'max_hr': str(max_hr), 'avg_rr': str(avg_rr)}]
             return jsonify(response), 200
         else:
             return {'message': 'invalid parameters'}, 400


if __name__ == '__main__':
    app.run(debug=True)