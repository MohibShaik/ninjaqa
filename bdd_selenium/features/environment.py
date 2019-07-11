import os 
environment = {
    "project":os.getenv("project","retail_suite_client"),
    "driver": os.getenv("driver", "chrome_v_75_win"),
    "environment":os.getenv("environment","local"),
    #pay_portal chrome_mac stage
}
