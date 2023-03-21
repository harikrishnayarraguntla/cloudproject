# cloudproject
Lightweight Policy Update Scheme Project

Description:
The proposed system utilizes AWS S3 (Simple Storage Service) to store the PHR data, and AWS KMS (Key Management Service) for key management and encryption. The lightweight policy update scheme is implemented using AWS Lambda, which enables the automatic execution of code in response to events.
The policy update process is initiated by an event trigger, such as a change in the privacy policy or the addition of a new healthcare provider. The Lambda function then updates the policy hash chain and generates a new policy key using ABE. The policy key is used to encrypt the PHR data, and the encrypted data is stored in the S3 bucket.
The proposed system also includes a web-based user interface for healthcare providers to manage access to the PHR data. The user interface allows healthcare providers to view the privacy policy, request access to specific PHR data, and grant access to other healthcare providers.
Overall, the proposed lightweight policy update scheme for outsourced PHR sharing using AWS provides a secure and scalable solution for managing and sharing sensitive healthcare data. It leverages the power of AWS cloud technology to ensure data privacy and confidentiality, while also providing a user-friendly interface for healthcare providers to manage access to the PHR data.
Eventually, we carried out the performance review to show how effective the suggested plan is. Our suggested method is based on proxy re-encryption and cipher text policy attribute-based encryption (CP-ABE) (PRE). To ensure complete traceability of policy changes, we also develop a policy versioning approach.
Services:
Services we are using in this project is EC2 services in AWS cloud.
About EC2:
Amazon Elastic Compute Cloud (EC2) is a web service offered by Amazon Web Services (AWS) that provides scalable computing capacity in the cloud. EC2 allows users to create virtual machines, also known as instances, in the cloud and configure them with the desired operating system, application stack, and security settings.
EC2 instances can be launched on-demand, which means that they can be started and stopped as per the user's requirements, and the user only pays for the time the instance is running. Additionally, EC2 instances can also be purchased as Reserved Instances, which provide a significant discount for longer-term usage.
Challenges:
Outsourced Personal Health Records (PHRs) are becoming increasingly popular as a way for individuals to store and share their medical information with healthcare providers and other authorized parties. However, maintaining the privacy and security of this sensitive information is a critical concern. A Lightweight Policy Update Scheme (LPUS) can be an effective way to manage access control policies for outsourced PHRs.
Securities about Hospitality:
Security is an important consideration in the hospitality industry to ensure the safety and well-being of guests and employees. Here are some tips for ensuring security in hospitality:
1.Conduct background checks: Conduct thorough background checks on all employees, including criminal history, employment history, and references. This will help to prevent the hiring of individuals with a history of theft or violence.
2.Install security cameras: Install security cameras in common areas and entrances to the property. This will help to deter criminal activity and can assist in identifying perpetrators in the event of a crime.
3.Implement access control: Implement access control measures such as key card systems and security guards to ensure that only authorized individuals have access to guest rooms and other restricted areas.
4.Train employees: Train employees on security protocols and procedures, including how to respond to emergencies and how to identify suspicious activity.
5.Secure guest information: Ensure that guest information is kept secure, including credit card information and personal identification details.
Tasks accomplished successfully:
Overall, implementing a Lightweight Policy Update Scheme for Outsourced Personal Health Records sharing requires careful planning, design, and implementation to ensure that the LPUS system functions effectively, efficiently, and securely.
1.System Analysis: The first step is to analyze the requirements of the LPUS system, including the necessary policies and access control mechanisms. This analysis should identify the key stakeholders and their roles, as well as the types of data that will be stored in the PHRs and the potential risks and vulnerabilities associated with that data.
2.Policy Design: Based on the analysis, the LPUS policies and access control mechanisms should be designed. This includes determining the access control rules for different types of data and the criteria for granting or revoking access to PHRs. The policies should also include rules for handling updates and changes to the policies themselves.
3.System Implementation: Once the LPUS policies and access control mechanisms have been designed, the LPUS system should be implemented. This includes developing the software and hardware infrastructure necessary to support the LPUS system, including servers, databases, and user interfaces.
4.Policy Update Management: The LPUS system should be able to handle policy updates efficiently and in real-time. This requires the development of an effective policy update management framework that can handle policy changes and revisions quickly and efficiently.
5.Security Management: Security is a critical concern in PHR sharing, and the LPUS system should be designed to prevent unauthorized access, data breaches, and other security risks. This includes developing security management procedures to monitor and control access to the LPUS system and the PHRs themselves.
