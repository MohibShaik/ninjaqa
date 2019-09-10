
from django.template.response import TemplateResponse
from django.shortcuts import render
import json
from reports.models import Report
from configuration.models import Project,Environment
from reports.models import Report
import os
import subprocess
from django.http import JsonResponse
from datetime import datetime

from bdd_selenium.features.environment import environment
try:

    project = Project.objects.get(name=environment['project'])
    global_project = Project.objects.get(name=environment['project'])
    global_environment = Environment.objects.get(project=project, environment=environment['environment'])
except:
	pass
from django.contrib.auth.decorators import login_required
@login_required
def runs(request, run_id=None):
    report=report_json=None
    failed_features=passed_features=failed_scenarios=passed_scenarios=notdefined_scenarios=skipped_secenarios=0
    
    bdd_path = os.path.abspath(".").split("ninjaqa")[0]+"ninjaqa/bdd_selenium/"
    print(bdd_path)
    if run_id:
        report = Report.objects.get(pk=run_id)
        print("..............................")
        print(report)
        with open(bdd_path+report.report_file) as f:
            report_json = eval(f.read())
            failed_features = len([e for e in report_json if e['status']=='failed'])
            passed_features = len([e for e in report_json if e['status']=='passed'])
            all_scenarios  = [e['elements'] for e in report_json]
            for scen_list in all_scenarios:
                for scen in  scen_list:
                    if scen['status']=='passed':
                        passed_scenarios=passed_scenarios+1  
                    elif scen['status']=='failed':
                        failed_scenarios=passed_scenarios+1  
                    elif scen['status']=='notdefined':
                        notdefined_scenarios=notdefined_scenarios+1  
                    elif scen['status']=='skipped':
                        skipped_secenarios=skipped_secenarios+1  
    reports = Report.objects.all()
    print(reports)

    reports = [e for e  in reports if os.path.exists(bdd_path+e.report_file) and open(bdd_path+e.report_file).read()]
    print(reports)
    # Passed features
    # [e['status'] for e in report_json]
    return TemplateResponse(request, 'runs.html', 
                {
                    "selected_page":"runs",
                    "run_id":run_id and int(run_id) or 0,
                    "reports": reports,
                    "report":report,
                    "generated_on":report and report.report_file[12:22] or None,
                    "report_json":report_json,
                    "environment":environment,
                    "failed_features":failed_features,
                    "passed_features":passed_features,
                    "failed_scenarios":failed_scenarios,
                    "passed_scenarios":passed_scenarios,
                    "notdefined_scenarios":notdefined_scenarios,
                    "skipped_secenarios":skipped_secenarios,
                    "feature_sections":[
                            {
                                "feture_id":"collapseFeature0"
                            },
                            {
                                "feture_id":"collapseFeature1"

                            }
                    ]
                }
        )

@login_required
def runsuite(request):
    return TemplateResponse(request, 'run_page.html', {"selected_page":"runsuite"})  

@login_required
def run_test_case(request):
    report_name=request.GET.get('report_name')
    details=request.GET.get('details')
    tm = str(datetime.now())[:19].replace(":",'-')
    if 'bdd_selenium' not in os.getcwd():
        os.chdir('bdd_selenium')
    fl='runs/report-%s.json'%tm
    f=open(fl,'w')
    f.close()

    subprocess.Popen(['python', '-m', 'behave', '-f', 'json', '-o',
                      fl], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    Report(environment=global_environment,report_name=report_name,
        details=details,run_by=request.user,
        report_file=fl).save()
    return JsonResponse({'status': 'Ran', 'tm': fl})
