"""This module contains the the default resources that Fideslang ships with."""

from fideslang import (
    DataCategory,
    DataQualifier,
    DataSubject,
    DataUse,
    Organization,
    Taxonomy,
)

DEFAULT_TAXONOMY = Taxonomy(
    data_category=[
        DataCategory(
            fides_key="user.payment",
            organization_fides_key="default_organization",
            name="Payment Data",
            description="Payment data related to user.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.payment.financial_account_number",
            organization_fides_key="default_organization",
            name="Account Payment Financial Account Number",
            description="Financial account number for an account's payment card, bank account, or other financial system.",
            parent_key="user.payment",
        ),
        DataCategory(
            fides_key="system",
            organization_fides_key="default_organization",
            name="System Data",
            description="Data unique to, and under control of the system.",
            parent_key=None,
        ),
        DataCategory(
            fides_key="system.authentication",
            organization_fides_key="default_organization",
            name="Authentication Data",
            description="Data used to manage access to the system.",
            parent_key="system",
        ),
        DataCategory(
            fides_key="system.operations",
            organization_fides_key="default_organization",
            name="Operations Data",
            description="Data used for system operations.",
            parent_key="system",
        ),
        DataCategory(
            fides_key="user",
            organization_fides_key="default_organization",
            name="User Data",
            description="Data related to the user of the system, either provided directly or derived based on their usage.",
            parent_key=None,
        ),
        DataCategory(
            fides_key="user.biometric",
            organization_fides_key="default_organization",
            name="Biometric Data",
            description="Encoded characteristics provided by a user.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.biometric_health",
            organization_fides_key="default_organization",
            name="Biometric Health Data",
            description="Encoded characteristic collected about a user.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.browsing_history",
            organization_fides_key="default_organization",
            name="Browsing History",
            description="Content browsing history of a user.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.demographic",
            organization_fides_key="default_organization",
            name="Demographic Data",
            description="Demographic data about a user.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.contact",
            organization_fides_key="default_organization",
            name="Contact Data",
            description="Contact data collected about a user.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.contact.address",
            organization_fides_key="default_organization",
            name="Contact Data",
            description="Contact address data collected about a user.",
            parent_key="user.contact",
        ),
        DataCategory(
            fides_key="user.device",
            organization_fides_key="default_organization",
            name="Device Data",
            description="Data related to a user's device, configuration and setting.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.device.cookie_id",
            organization_fides_key="default_organization",
            name="Cookie ID",
            description="Cookie unique identification number.",
            parent_key="user.device",
        ),
        DataCategory(
            fides_key="user.device.device_id",
            organization_fides_key="default_organization",
            name="Device ID",
            description="Device unique identification number.",
            parent_key="user.device",
        ),
        DataCategory(
            fides_key="user.device.ip_address",
            organization_fides_key="default_organization",
            name="IP Address",
            description="Unique identifier related to device connection.",
            parent_key="user.device",
        ),
        DataCategory(
            fides_key="user.nonidentifiable",
            organization_fides_key="default_organization",
            name="User Non-Identifiable Data",
            description="Non-user identifiable data related to a user as a result of user actions in the system.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.gender",
            organization_fides_key="default_organization",
            name="Gender",
            description="Gender of an individual.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.location",
            organization_fides_key="default_organization",
            name="Location Data",
            description="Records of the location of a user.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.media_consumption",
            organization_fides_key="default_organization",
            name="Media Consumption Data",
            description="Media type consumption data of a user.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.non_specific_age",
            organization_fides_key="default_organization",
            name="Non-Specific Age",
            description="Age range data.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.observed",
            organization_fides_key="default_organization",
            name="Observed Data",
            description="Data collected through observation of use of the system.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.profiling",
            organization_fides_key="default_organization",
            name="Profiling Data",
            description="Preference and interest data about a user.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.race",
            organization_fides_key="default_organization",
            name="Race",
            description="Racial or ethnic origin data.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.religious_belief",
            organization_fides_key="default_organization",
            name="Religious Belief",
            description="Religion or religious belief.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.search_history",
            organization_fides_key="default_organization",
            name="Search History",
            description="Records of search history and queries of a user.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.sexual_orientation",
            organization_fides_key="default_organization",
            name="Sexual Orientation",
            description="Personal sex life or sexual data.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.social",
            organization_fides_key="default_organization",
            name="Social Data",
            description="Social activity and interaction data.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.telemetry",
            organization_fides_key="default_organization",
            name="Telemetry Data",
            description="User identifiable measurement data from system sensors and monitoring.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.unique_id",
            organization_fides_key="default_organization",
            name="Unique ID",
            description="Unique identifier for a user assigned through system use.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.user_sensor",
            organization_fides_key="default_organization",
            name="User Sensor Data",
            description="Measurement data about a user's environment through system use.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.organization",
            organization_fides_key="default_organization",
            name="Organization Identifiable Data",
            description="Data that is linked to, or identifies an organization.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.workplace",
            organization_fides_key="default_organization",
            name="Workplace",
            description="Organization of employment.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.sensor",
            organization_fides_key="default_organization",
            name="Sensor Data",
            description="Measurement data from sensors and monitoring systems.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.childrens",
            organization_fides_key="default_organization",
            name="Children's Data",
            description="Data relating to children.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.contact.address.city",
            organization_fides_key="default_organization",
            name="User Contact City",
            description="User's city level address data.",
            parent_key="user.contact.address",
        ),
        DataCategory(
            fides_key="user.contact.address.country",
            organization_fides_key="default_organization",
            name="User Contact Country",
            description="User's country level address data.",
            parent_key="user.contact.address",
        ),
        DataCategory(
            fides_key="user.contact.email",
            organization_fides_key="default_organization",
            name="User Contact Email",
            description="User's contact email address.",
            parent_key="user.contact",
        ),
        DataCategory(
            fides_key="user.contact.phone_number",
            organization_fides_key="default_organization",
            name="User Contact Phone Number",
            description="User's phone number.",
            parent_key="user.contact",
        ),
        DataCategory(
            fides_key="user.contact.address.postal_code",
            organization_fides_key="default_organization",
            name="User Contact Postal Code",
            description="User's postal code.",
            parent_key="user.contact.address",
        ),
        DataCategory(
            fides_key="user.contact.address.state",
            organization_fides_key="default_organization",
            name="User Contact State",
            description="User's state level address data.",
            parent_key="user.contact.address",
        ),
        DataCategory(
            fides_key="user.contact.address.street",
            organization_fides_key="default_organization",
            name="User Contact Street",
            description="User's street level address data.",
            parent_key="user.contact.address",
        ),
        DataCategory(
            fides_key="user.credentials",
            organization_fides_key="default_organization",
            name="Credentials",
            description="User authentication data.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.credentials.biometric_credentials",
            organization_fides_key="default_organization",
            name="Biometric Credentials",
            description="Credentials for system authentication.",
            parent_key="user.credentials",
        ),
        DataCategory(
            fides_key="user.credentials.password",
            organization_fides_key="default_organization",
            name="Password",
            description="Password for system authentication.",
            parent_key="user.credentials",
        ),
        DataCategory(
            fides_key="user.date_of_birth",
            organization_fides_key="default_organization",
            name="Date of Birth",
            description="User's date of birth.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.financial",
            organization_fides_key="default_organization",
            name="Financial Data",
            description="Payment data and financial history.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.financial.account_number",
            organization_fides_key="default_organization",
            name="User Financial Account Number",
            description="User's account number for a payment card, bank account, or other financial system.",
            parent_key="user.financial",
        ),
        DataCategory(
            fides_key="user.genetic",
            organization_fides_key="default_organization",
            name="Genetic Data",
            description="Data about the genetic makeup provided by a user.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.government_id",
            organization_fides_key="default_organization",
            name="Government ID",
            description="State provided identification data.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.government_id.drivers_license_number",
            organization_fides_key="default_organization",
            name="Driver's License Number",
            description="State issued driving identification number.",
            parent_key="user.government_id",
        ),
        DataCategory(
            fides_key="user.government_id.national_identification_number",
            organization_fides_key="default_organization",
            name="National Identification Number",
            description="State issued personal identification number.",
            parent_key="user.government_id",
        ),
        DataCategory(
            fides_key="user.government_id.passport_number",
            organization_fides_key="default_organization",
            name="Passport Number",
            description="State issued passport data.",
            parent_key="user.government_id",
        ),
        DataCategory(
            fides_key="user.health_and_medical",
            organization_fides_key="default_organization",
            name="Health and Medical Data",
            description="Health records or individual's personal medical information.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.job_title",
            organization_fides_key="default_organization",
            name="Job Title",
            description="Professional data.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.name",
            organization_fides_key="default_organization",
            name="Name",
            description="User's real name.",
            parent_key="user",
        ),
        DataCategory(
            fides_key="user.political_opinion",
            organization_fides_key="default_organization",
            name="Political Opinion",
            description="Data related to the individual's political opinions.",
            parent_key="user",
        ),
    ],
    data_subject=[
        DataSubject(
            fides_key="anonymous_user",
            organization_fides_key="default_organization",
            name="Anonymous User",
            description="An individual that is unidentifiable to the systems. Note - This should only be applied to truly anonymous users where there is no risk of re-identification",
        ),
        DataSubject(
            fides_key="citizen_voter",
            organization_fides_key="default_organization",
            name="Citizen Voter",
            description="An individual registered to voter with a state or authority.",
        ),
        DataSubject(
            fides_key="commuter",
            organization_fides_key="default_organization",
            name="Commuter",
            description="An individual that is traveling or transiting in the context of location tracking.",
        ),
        DataSubject(
            fides_key="consultant",
            organization_fides_key="default_organization",
            name="Consultant",
            description="An individual employed in a consultative/temporary capacity by the organization.",
        ),
        DataSubject(
            fides_key="customer",
            organization_fides_key="default_organization",
            name="Customer",
            description="An individual or other organization that purchases goods or services from the organization.",
        ),
        DataSubject(
            fides_key="employee",
            organization_fides_key="default_organization",
            name="Employee",
            description="An individual employed by the organization.",
        ),
        DataSubject(
            fides_key="job_applicant",
            organization_fides_key="default_organization",
            name="Job Applicant",
            description="An individual applying for employment to the organization.",
        ),
        DataSubject(
            fides_key="next_of_kin",
            organization_fides_key="default_organization",
            name="Next of Kin",
            description="A relative of any other individual subject where such a relationship is known.",
        ),
        DataSubject(
            fides_key="passenger",
            organization_fides_key="default_organization",
            name="Passenger",
            description="An individual traveling on some means of provided transport.",
        ),
        DataSubject(
            fides_key="patient",
            organization_fides_key="default_organization",
            name="Patient",
            description="An individual identified for the purposes of any medical care.",
        ),
        DataSubject(
            fides_key="prospect",
            organization_fides_key="default_organization",
            name="Prospect",
            description="An individual or organization to whom an organization is selling goods or services.",
        ),
        DataSubject(
            fides_key="shareholder",
            organization_fides_key="default_organization",
            name="Shareholder",
            description="An individual or organization that holds equity in the organization.",
        ),
        DataSubject(
            fides_key="supplier_vendor",
            organization_fides_key="default_organization",
            name="Supplier/Vendor",
            description="An individual or organization that provides services or goods to the organization.",
        ),
        DataSubject(
            fides_key="trainee",
            organization_fides_key="default_organization",
            name="Trainee",
            description="An individual undergoing training by the organization.",
        ),
        DataSubject(
            fides_key="visitor",
            organization_fides_key="default_organization",
            name="Visitor",
            description="An individual visiting a location.",
        ),
    ],
    data_use=[
        DataUse(
            fides_key="provide",
            organization_fides_key="default_organization",
            name="Provide the capability",
            description="Provide, give, or make available the product, service, application or system.",
            parent_key=None,
        ),
        DataUse(
            fides_key="provide.service",
            organization_fides_key="default_organization",
            name="Service",
            description="The source service, system, or product being provided to the user.",
            parent_key="provide",
        ),
        DataUse(
            fides_key="provide.service.operations",
            organization_fides_key="default_organization",
            name="Service Operations",
            description="Use of specified data categories to operate and protect in order to provide the service.",
            parent_key="provide.service",
        ),
        DataUse(
            fides_key="provide.service.operations.support",
            organization_fides_key="default_organization",
            name="Operations Support",
            description="Use of specified data categories to provide support for operation and protection in order to provide the service.",
            parent_key="provide.service.operations",
        ),
        DataUse(
            fides_key="provide.service.operations.support.optimization",
            organization_fides_key="default_organization",
            name="Support Optimization",
            description="Use of specified data categories to optimize and improve support operations in order to provide the service.",
            parent_key="provide.service.operations.support",
        ),
        DataUse(
            fides_key="provide.service.upgrades",
            organization_fides_key="default_organization",
            name="Offer Upgrades",
            description="Offer upgrades or upsales such as increased capacity for the service based on monitoring of service usage.",
            parent_key="provide.service",
        ),
        DataUse(
            fides_key="improve",
            organization_fides_key="default_organization",
            name="Improve the capability",
            description="Improve the product, service, application or system.",
            parent_key=None,
        ),
        DataUse(
            fides_key="improve.system",
            organization_fides_key="default_organization",
            name="System",
            description="The source system, product, service or application being improved.",
            parent_key="improve",
        ),
        DataUse(
            fides_key="personalize",
            organization_fides_key="default_organization",
            name="Personalize the capability",
            description="Personalize the product, service, application or system.",
            parent_key=None,
        ),
        DataUse(
            fides_key="personalize.system",
            organization_fides_key="default_organization",
            name="System",
            description="The source system, product, service or application being personalized.",
            parent_key="personalize",
        ),
        DataUse(
            fides_key="advertising",
            organization_fides_key="default_organization",
            name="Advertising, Marketing or Promotion",
            description="The promotion of products or services targeted to users based on the the processing of user provided data in the system.",
            parent_key=None,
        ),
        DataUse(
            fides_key="advertising.first_party",
            organization_fides_key="default_organization",
            name="First Party Advertising",
            description="The promotion of products or services targeting users based on processing of derviced data from prior use of the system.",
            parent_key="advertising",
        ),
        DataUse(
            fides_key="advertising.third_party",
            organization_fides_key="default_organization",
            name="Third Party Advertising",
            description="The promotion of products or services targeting users based on processing of specific categories of data acquired from third party sources.",
            parent_key="advertising",
        ),
        DataUse(
            fides_key="advertising.first_party.contextual",
            organization_fides_key="default_organization",
            name="First Party Contextual Advertising",
            description="The promotion of products or services targeted to users based on the processing of data from the users prior use of the services.",
            parent_key="advertising.first_party",
        ),
        DataUse(
            fides_key="advertising.first_party.personalized",
            organization_fides_key="default_organization",
            name="First Party Personalized Advertising",
            description="The targeting and changing of promotional content based on processing of specific data categories from the user.",
            parent_key="advertising.first_party",
        ),
        DataUse(
            fides_key="advertising.third_party.personalized",
            organization_fides_key="default_organization",
            name="Third Party Personalized Advertising",
            description="The targeting and changing of promotional content based on processing of specific categories of user data acquired from third party sources.",
            parent_key="advertising.third_party",
        ),
        DataUse(
            fides_key="third_party_sharing",
            organization_fides_key="default_organization",
            name="Third Party Sharing",
            description="The transfer of specified data categories to third parties outside of the system/application's scope.",
            parent_key=None,
        ),
        DataUse(
            fides_key="third_party_sharing.payment_processing",
            organization_fides_key="default_organization",
            name="Sharing for Processing Payments",
            description="Sharing of specified data categories with a third party for payment processing.",
            parent_key="third_party_sharing",
        ),
        DataUse(
            fides_key="third_party_sharing.personalized_advertising",
            organization_fides_key="default_organization",
            name="Sharing for Personalized Advertising",
            description="Sharing of specified data categories for the purpose of marketing/advertising/promotion.",
            parent_key="third_party_sharing",
        ),
        DataUse(
            fides_key="third_party_sharing.fraud_detection",
            organization_fides_key="default_organization",
            name="Sharing for Fraud Detection",
            description="Sharing of specified data categories with a third party fo fraud prevention/detection.",
            parent_key="third_party_sharing",
        ),
        DataUse(
            fides_key="third_party_sharing.legal_obligation",
            organization_fides_key="default_organization",
            name="Sharing for Legal Obligation",
            description="Sharing of data for legal obligations, including contracts, applicable laws or regulations.",
            parent_key="third_party_sharing",
        ),
        DataUse(
            fides_key="collect",
            organization_fides_key="default_organization",
            name="Collect",
            description="Collecting and storing data in order to use it for another purpose such as data training for ML.",
            parent_key=None,
        ),
        DataUse(
            fides_key="train_ai_system",
            organization_fides_key="default_organization",
            name="Train AI System",
            description="Training an AI system. Please note when this data use is specified, the method and degree to which a user may be directly identified in the resulting AI system should be appended.",
            parent_key=None,
        ),
    ],
    data_qualifier=[
        DataQualifier(
            fides_key="aggregated",
            organization_fides_key="default_organization",
            name="Aggregated Data",
            description="Statistical data that does not contain individually identifying information but includes information about groups of individuals that renders individual identification impossible.",
            parent_key=None,
        ),
        DataQualifier(
            fides_key="aggregated.anonymized",
            organization_fides_key="default_organization",
            name="Anonymized Data",
            description="Data where all attributes have been sufficiently altered that the individaul cannot be reidentified by this data or in combination with other datasets.",
            parent_key="aggregated",
        ),
        DataQualifier(
            fides_key="aggregated.anonymized.unlinked_pseudonymized",
            organization_fides_key="default_organization",
            name="Unlinked Pseudonymized Data",
            description="Data for which all identifiers have been substituted with unrelated values and linkages broken such that it may not be reversed, even by the party that performed the pseudonymization.",
            parent_key="aggregated.anonymized",
        ),
        DataQualifier(
            fides_key="aggregated.anonymized.unlinked_pseudonymized.pseudonymized",
            organization_fides_key="default_organization",
            name="Pseudonymized Data",
            description="Data for which all identifiers have been substituted with unrelated values, rendering the individual unidentifiable and cannot be reasonably reversed other than by the party that performed the pseudonymization.",
            parent_key="aggregated.anonymized.unlinked_pseudonymized",
        ),
        DataQualifier(
            fides_key="aggregated.anonymized.unlinked_pseudonymized.pseudonymized.identified",
            organization_fides_key="default_organization",
            name="Identified Data",
            description="Data that directly identifies an individual.",
            parent_key="aggregated.anonymized.unlinked_pseudonymized.pseudonymized",
        ),
    ],
    organization=[Organization(fides_key="default_organization")],
)
