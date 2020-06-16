import os

project_path = os.path.split(os.path.realpath(__file__))[0]

conf_path = os.path.join(project_path, r'conf\case.config')
test_data_path = os.path.join(project_path, r'test_Data\data.xlsx')
test_result_html_path = os.path.join(project_path, r'test_result\html_report\test.html')
