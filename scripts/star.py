#############################################################################################################################################################
#														Created by Sandip Pramanik(367544)																	#
#############################################################################################################################################################

#!/usr/bin/python
from java.io import FileInputStream
import time

propInputStream= FileInputStream('weblogic.properties')
configProps = Properties()
configProps.load(propInputStream)

adminURL= configProps.get('admin.url')
adminUserName= configProps.get('admin.username')
adminPassword= configProps.get('admin.password')
total_jndi_to_create=configProps.get('total.FTPjndi')

appName='FtpAdapter'
moduleOverrideName=appName+'.rar'
moduleDescriptorName='META-INF/weblogic-ra.xml'

planPath = configProps.get('shared_FTP_PlanPath')
appPath = configProps.get('FTP_appPath')


def makeDeploymentPlanVariable(wlstPlan, name, value, xpath, origin='planbased'):
  """Create a varaible in the Plan.
  This method is used to create the variables that are needed in the Plan in order
  to add an entry for the outbound connection pool for the new data source.
  """
 
  try:

    variableAssignment = wlstPlan.createVariableAssignment(name, moduleOverrideName, moduleDescriptorName)
    variableAssignment.setXpath(xpath)
    variableAssignment.setOrigin(origin)
    wlstPlan.createVariable(name, value)
 
  except:
    print('--> was not able to create deployment plan variables successfully')
 
def main():
 
  #
  # generate a unique string to use in the names
  #
  uniqueString =''
  uniqueString = str(int(time.time()))
 
  #
  # Create a JDBC Data Source.
  #
 
  try:
    print('--> about to connect to weblogic')
    connect(adminUserName, adminPassword, adminURL)
    edit()

#
# update the deployment plan
#
    startEdit()
    i=1
    while (i <= int(total_jndi_to_create)):
	cd('/')
	print('--> about to update the deployment plan for the FtpAdapter')
	eisName = configProps.get('FTP_eisName.'+ str(i))
	print('--> about to create a Adapter JNDI ' + eisName)
	Host = configProps.get("FTP_host."+ str(i))
	print('--> about to assign a FTP host ' + Host)
	userName = configProps.get("FTP_username."+ str(i))
	print('--> about to assign a FTP userName ' + userName)
	Port = configProps.get("FTP_port."+ str(i))
	print('--> about to assign FTP port ' + Port)
	Password = configProps.get("FTP_password."+ str(i))
	print('--> about to assign FTP Password ' + Password)
	UseSftp = configProps.get("FTP_useSftp."+ str(i))
	print('--> about to assign FTP UseSftp ' + UseSftp)
	ControlDir = configProps.get("FTP_controlDir."+ str(i))
	print('--> about to assign FTP controlDir ' + ControlDir)
	InboundDataSource = configProps.get("FTP_inboundDataSource."+ str(i))
	print('--> about to assign FTP inboundDataSource ' + InboundDataSource)
	OutboundDataSource = configProps.get("FTP_outboundDataSource."+ str(i))
	print('--> about to assign FTP outboundDataSource ' + OutboundDataSource)
	OutboundDataSourceLocal = configProps.get("FTP_outboundDataSourceLocal."+ str(i))
	print('--> about to assign FTP outboundDataSourceLocal ' + OutboundDataSourceLocal)
	AuthenticationType = configProps.get("FTP_authenticationType."+ str(i))
	print('--> about to assign FTP authenticationType ' + AuthenticationType)
	ChangeDirectory = configProps.get("FTP_changeDirectory."+ str(i))
	print('--> about to assign FTP changeDirectory ' + ChangeDirectory)
	EnforceFileTypeFromSpec = configProps.get("FTP_enforceFileTypeFromSpec."+ str(i))
	print('--> about to assign FTP enforceFileTypeFromSpec ' + EnforceFileTypeFromSpec)
	FtpAbsolutePathBegin = configProps.get("FTP_ftpAbsolutePathBegin."+ str(i))
	print('--> about to assign FTP ftpAbsolutePathBegin ' + FtpAbsolutePathBegin)
	FtpPathSeparator = configProps.get("FTP_ftpPathSeparator."+ str(i))
	print('--> about to assign FTP ftpPathSeparator ' + FtpPathSeparator)
	IgnorePermissionsOnFile = configProps.get("FTP_ignorePermissionsOnFile."+ str(i))
	print('--> about to assign FTP ignorePermissionsOnFile ' + IgnorePermissionsOnFile)
	PreferredCipherSuite = configProps.get("FTP_preferredCipherSuite."+ str(i))
	print('--> about to assign FTP preferredCipherSuite ' + PreferredCipherSuite)
	PrivateKeyFile = configProps.get("FTP_privateKeyFile."+ str(i))
	print('--> about to assign FTP privateKeyFile ' + PrivateKeyFile)
	WorkingDirectory = configProps.get("FTP_workingDirectory."+ str(i))
	print('--> about to assign FTP workingDirectory ' + WorkingDirectory)
	
	
	startEdit()
	print('--> Using plan ' + planPath)
	plan = loadApplication(appPath, planPath)
	print('--> adding variables to plan')
	print '___ BEGIN change plan'
	makeDeploymentPlanVariable(plan, 'ConnectionInstance_'+ eisName +'_JNDIName_'+ uniqueString, eisName, 	'/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ eisName + '"]/jndi-name')
	makeDeploymentPlanVariable(plan, 'ConfigProperty_xADataSourceName_'+ Host + '_',Host, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ eisName + '"]/connection-properties/properties/property/[name="host"]/value')
	makeDeploymentPlanVariable(plan, 'ConfigProperty_xADataSourceName_'+ Password + '_',Password, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ eisName + '"]/connection-properties/properties/property/[name="password"]/value')
	makeDeploymentPlanVariable(plan, 'ConfigProperty_xADataSourceName_'+ Port + '_',Port, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ eisName + '"]/connection-properties/properties/property/[name="port"]/value')
	makeDeploymentPlanVariable(plan, 'ConfigProperty_xADataSourceName_'+ userName + '_',userName, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ eisName + '"]/connection-properties/properties/property/[name="username"]/value')
	makeDeploymentPlanVariable(plan, 'ConfigProperty_xADataSourceName_'+ UseSftp + '_',UseSftp, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ eisName + '"]/connection-properties/properties/property/[name="useSftp"]/value')
	makeDeploymentPlanVariable(plan, 'ConfigProperty_xADataSourceName_'+ ControlDir + '_',ControlDir, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ eisName + '"]/connection-properties/properties/property/[name="controlDir"]/value')
	makeDeploymentPlanVariable(plan, 'ConfigProperty_xADataSourceName_'+ InboundDataSource + '_',InboundDataSource, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ eisName + '"]/connection-properties/properties/property/[name="inboundDataSource"]/value')
	makeDeploymentPlanVariable(plan, 'ConfigProperty_xADataSourceName_'+ OutboundDataSource + '_',OutboundDataSource, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ eisName + '"]/connection-properties/properties/property/[name="outboundDataSource"]/value')
	makeDeploymentPlanVariable(plan, 'ConfigProperty_xADataSourceName_'+ OutboundDataSourceLocal + '_',OutboundDataSourceLocal, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ eisName + '"]/connection-properties/properties/property/[name="outboundDataSourceLocal"]/value')
	makeDeploymentPlanVariable(plan, 'ConfigProperty_xADataSourceName_'+ ChangeDirectory + '_',ChangeDirectory, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ eisName + '"]/connection-properties/properties/property/[name="changeDirectory"]/value')
	makeDeploymentPlanVariable(plan, 'ConfigProperty_xADataSourceName_'+ EnforceFileTypeFromSpec + '_',EnforceFileTypeFromSpec, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ eisName + '"]/connection-properties/properties/property/[name="enforceFileTypeFromSpec"]/value')
	makeDeploymentPlanVariable(plan, 'ConfigProperty_xADataSourceName_'+ FtpAbsolutePathBegin + '_',FtpAbsolutePathBegin, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ eisName + '"]/connection-properties/properties/property/[name="ftpAbsolutePathBegin"]/value')
	makeDeploymentPlanVariable(plan, 'ConfigProperty_xADataSourceName_'+ FtpPathSeparator + '_',FtpPathSeparator, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ eisName + '"]/connection-properties/properties/property/[name="ftpPathSeparator"]/value')
	makeDeploymentPlanVariable(plan, 'ConfigProperty_xADataSourceName_'+ IgnorePermissionsOnFile + '_',IgnorePermissionsOnFile, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ eisName + '"]/connection-properties/properties/property/[name="ignorePermissionsOnFile"]/value')
	makeDeploymentPlanVariable(plan, 'ConfigProperty_xADataSourceName_'+ PreferredCipherSuite + '_',PreferredCipherSuite, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ eisName + '"]/connection-properties/properties/property/[name="preferredCipherSuite"]/value')
	makeDeploymentPlanVariable(plan, 'ConfigProperty_xADataSourceName_'+ PrivateKeyFile + '_',PrivateKeyFile, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ eisName + '"]/connection-properties/properties/property/[name="privateKeyFile"]/value')
	makeDeploymentPlanVariable(plan, 'ConfigProperty_xADataSourceName_'+ WorkingDirectory + '_',WorkingDirectory, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ eisName + '"]/connection-properties/properties/property/[name="workingDirectory"]/value')
	makeDeploymentPlanVariable(plan, 'ConfigProperty_xADataSourceName_'+ AuthenticationType + '_',AuthenticationType, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ eisName + '"]/connection-properties/properties/property/[name="authenticationType"]/value')
	print '___ DONE change plan'
	print('--> saving plan')
	plan.save();
	save();
	
	print('--> activating changes')
	activate(block='true');
	
	cd('/AppDeployments/FtpAdapter/Targets');
	print('--> redeploying the FtpAdapter')
 	
	redeploy(appName, planPath, targets=cmo.getTargets());
	print('--> done')
	i=i+1
		
  except:
    		print('--> something went wrong, bailing out')
    		stopEdit('y')
    		raise SystemExit

main()