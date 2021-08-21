import boto3

REGION_NAME='sa-east-1'
client = boto3.client('ec2',region_name=REGION_NAME)

#print("teste")
print("Instances Information:")
for instances in client.describe_instances()['Reservations']:
      for instance in instances['Instances']:
            print('InstanceId:' ,(instance['InstanceId']))
            print('InstanceType:' ,(instance['InstanceType']))
            print('KeyName:' ,(instance['KeyName']))
            print('LaunchTime:' ,(instance['LaunchTime']))
            print('Placement:' ,(instance['Placement']))
            print('SubnetId:' ,(instance['SubnetId']))
            print('VPCId' ,(instance['VpcId']))
            print('SecurityGroups:' ,(instance['SecurityGroups']))
            print('Tags:' ,(instance['Tags']))
            print('\n')
print("Security Group Information:")
for sgs in client.describe_security_groups()['SecurityGroups']:
      #for sg in sgs['0']:
      print('Description:' ,(sgs['Description']))
      print('SecurityGroupID' ,(sgs['GroupId']))
      print('SecurityGroupName' ,(sgs['GroupName']))
      print('IpPermissions:' ,(sgs['IpPermissions']))
      print('VPCId:' ,(sgs['VpcId']))
      print('\n')
print("VPCs Information:")      
for vpcs in client.describe_vpcs()['Vpcs']:
      print('CIDR Block:' ,(vpcs['CidrBlock']))
      print('State:' ,(vpcs['State']))
      print('VpcId:' ,(vpcs['VpcId']))
      print('OwnderId:' ,(vpcs['OwnerId']))
      print('\n')
print("Route Tables Information:")          
for routes in client.describe_route_tables()['RouteTables']:           
      print('Associations:' ,(routes['Associations']))
      print('RouteTableId:' ,(routes['RouteTableId']))      
      print('VpcId:' ,(routes['VpcId']))
      print('OwnerId:' ,(routes['OwnerId']))
      print('\n')
print("NACL Information:")      
for nacls in client.describe_network_acls()['NetworkAcls']:  
      print('Associations:' ,(nacls['Associations']))
      print('NetworkAclId:' ,(nacls['NetworkAclId']))
      print('SubnetId:' ,(nacls['VpcId']))
      print('OwnerId:' ,(nacls['OwnerId']))
      #print('CidrBlock:' ,(nacls['CidrBlock']))
      #print('Egress:' ,(nacls['Egress']))
      #print('RuleAction:' ,(nacls['RuleAction']))
      #print('RuleNumber:' ,(nacls['RuleNumber']))