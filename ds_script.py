#!/usr/bin/env python
import sys
sys.path.insert(0,'./deep-security-py')
import deepsecurity

mgr = deepsecurity.dsm.Manager(hostname='127.0.0.1', username='user', password='TrendMicro2016!', ignore_ssl_validation=True)
mgr.sign_in()
mgr.computers.get()

try:
    for computer_id in mgr.computers.find(overall_version='9.*|8.*'):
        computer = mgr.computers[computer_id]
        name = computer.name
        platform = computer.platform
        recommended_rules = computer.get_recommended_rules()
        overall_status= computer.overall_status
        overall_version = computer.overall_version
        overall_anti_malware_status = computer.overall_anti_malware_status
        overall_firewall_status = computer.overall_firewall_status
        overall_firewall_status = computer.overall_firewall_status
        overall_intrusion_prevention_status = computer.overall_intrusion_prevention_status
        overall_web_reputation_status = computer.overall_web_reputation_status
        overall_log_inspection_status = computer.overall_log_inspection_status
        print ("Computer_ID: %s" % computer_id)
        print ("Computer Name: %s" % name)
        print ("Platform: %s" % platform )
        print ("Get Recommended Rules: %s" % recommended_rules)
        print ("Overall Status: %s" % overall_status)
        print ("Overal Version: %s" % overall_version)
        print ("Overall Anti Malware Status: %s" % overall_anti_malware_status)
        print ("Overall Anti Firewall Status: %s" % overall_firewall_status)
        print ("Overall Anti IPS Status: %s" % overall_intrusion_prevention_status)
        print ("Overall Web Reputation Status: %s" % overall_web_reputation_status)
        print ("Overall Log Inspection Status: %s" % overall_log_inspection_status)
        print ("Clear Alerts and Warnings: %s" % computer.clear_alerts_and_warnings())
        print ("Get Recommended Rules: %s" % computer.get_recommended_rules())
        computer.send_events()
except Exception as e:
    print ("Error %s" % e)
    mgr.sign_out()
mgr.sign_out()
