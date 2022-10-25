import requests
import json
import pandas
import csv

link = "https://reportcard-rails.herokuapp.com/api/v1/lea_data"

df = pandas.read_csv('all_leas.csv')

with open('data_file.csv', 'w', newline='') as f:
  writer = csv.writer(f)

  header = [
    'lea_id',
    'district_name',
    'urban_centric_locale',
    'number_of_schools_in_district',
    'enrollment',
    'pre_k_teachers',
    'kindergarten_teachers',
    'elementary_teachers',
    'secondary_teachers',
    'total_teachers',
    'student_teacher_ratio',
    'instructional_aides',
    'guidance_counselors',
    'student_guidance_counselor_ratio',
    'librarian_total',
    'student_librarian_ratio',
    'total_staff',
    'district_expense_total',
    'expenses_for_instruction',
    'salaries_total',
    'salaries_instruction',
    'instruction_salary_percent_of_total',
    'per_student_expenditure',
    'per_teacher_salary_expenses'
  ]

  writer.writerow(header)

  # for i in range(1,len(df)):
  for i in range(0,len(df)):
    try:
      if len(df.values[i][0]) == 6:
        lea_id = "0" + str(df.values[i][0])
      else:
        lea_id = str(df.values[i][0])
      
      data = {
        "lea_id": lea_id
      }
      
      response = requests.post(link, json = data)
      
      x = response.text

      y = json.loads(x)

      to_be_written = [
        (y['data']['attributes'][0]['lea_id']),
        (y['data']['attributes'][1]['district_name']),
        (y['data']['attributes'][2]['urban_centric_locale']),
        (y['data']['attributes'][3]['number_of_schools_in_district']),
        (y['data']['attributes'][4]['enrollment']),
        (y['data']['attributes'][5]['pre_k_teachers']),
        (y['data']['attributes'][6]['kindergarten_teachers']),
        (y['data']['attributes'][7]['elementary_teachers']),
        (y['data']['attributes'][8]['secondary_teachers']),
        (y['data']['attributes'][9]['total_teachers']),
        (y['data']['attributes'][10]['student_teacher_ratio']),
        (y['data']['attributes'][11]['instructional_aides']),
        (y['data']['attributes'][12]['guidance_counselors']),
        (y['data']['attributes'][13]['student_guidance_counselor_ratio']),
        (y['data']['attributes'][14]['librarian_total']),
        (y['data']['attributes'][15]['student_librarian_ratio']),
        (y['data']['attributes'][16]['total_staff']),
        (y['data']['attributes'][17]['district_expense_total']),
        (y['data']['attributes'][18]['expenses_for_instruction']),
        (y['data']['attributes'][19]['salaries_total']),
        (y['data']['attributes'][20]['salaries_instruction']),
        (y['data']['attributes'][21]['instruction_salary_percent_of_total']),
        (y['data']['attributes'][22]['per_student_expenditure']),
        (y['data']['attributes'][23]['per_teacher_salary_expenses'])
      ]

      writer.writerow(to_be_written)

      print((y['data']['attributes'][1]['district_name']))

      if i % 10 == 0:
        print(f'------- {round(((i / len(df)) * 100),2)}% completed -------')
    except:
      pass