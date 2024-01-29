import boto3

def create_vpc(vpc_cidr_block, vpc_name):
    # Create a VPC
    ec2 = boto3.client('ec2', region_name='eu-west-3')
    response = ec2.create_vpc(CidrBlock=vpc_cidr_block)
    vpc_id = response['Vpc']['VpcId']
    
    # Add a name tag to the VPC
    ec2.create_tags(Resources=[vpc_id], Tags=[{'Key': 'Name', 'Value': vpc_name}])

    print(f'VPC {vpc_name} ({vpc_id}) created successfully.')

if __name__ == "__main__":
    # Replace these values with your desired CIDR block and VPC name
    vpc_cidr_block = '172.16.0.0/16'
    vpc_name = 'MyVPC'

    create_vpc(vpc_cidr_block, vpc_name)

