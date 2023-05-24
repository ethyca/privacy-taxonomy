from fideslang.models import DataUse

DEFAULT_DATA_USES = [
    # Analytics
    DataUse(
        fides_key="analytics",
        organization_fides_key="default_organization",
        name="Analytics",
        description="Analytics for activities such as system and advertising performance reporting, insights and fraud detection.",
        parent_key=None,
        is_default=True,
    ),
    DataUse(
        fides_key="analytics.reporting",
        organization_fides_key="default_organization",
        name="Analytics for Reporting",
        description="Analytics for general reporting such as system and advertising performance.",
        parent_key="analytics",
        is_default=True,
    ),
    DataUse(
        fides_key="analytics.reporting.ad_performance",
        organization_fides_key="default_organization",
        name="Analytics for Advertising Performance",
        description="Analytics for reporting of advertising performance.",
        parent_key="analytics.reporting",
        is_default=True,
    ),
    DataUse(
        fides_key="analytics.reporting.campaign_insights",
        organization_fides_key="default_organization",
        name="Analytics for Insights",
        description="Analytics for reporting of campaign insights related to advertising and promotion activities.",
        parent_key="analytics.reporting",
        is_default=True,
    ),
    DataUse(
        fides_key="analytics.reporting.system",
        organization_fides_key="default_organization",
        name="Analytics for System Activity",
        description="Analytics for reporting on system activity.",
        parent_key="analytics.reporting",
        is_default=True,
    ),
    DataUse(
        fides_key="analytics.reporting.system.performance",
        organization_fides_key="default_organization",
        name="Analytics for System Performance",
        description="Analytics for reporting on system performance.",
        parent_key="analytics.reporting.system",
        is_default=True,
    ),
    # Collect
    DataUse(
        fides_key="collect",
        organization_fides_key="default_organization",
        name="Collect",
        description="Collecting or storing data in order to use it for another purpose which has not yet been expressly defined.",
        parent_key=None,
        is_default=True,
    ),
    # Employment
    DataUse(
        fides_key="employment",
        name="Employment",
        organization_fides_key="default_organization",
        description="Processing of data for the purpose of recruitment or employment and human resources (HR) related activities.",
        parent_key=None,
        is_default=True,
    ),
    DataUse(
        fides_key="employment.recruitment",
        name="Employment Recruitment",
        organization_fides_key="default_organization",
        description="Processing of prospective employees for the purpose of recruitment.",
        parent_key="employment",
        is_default=True,
    ),
    # Essential
    DataUse(
        fides_key="essential",
        name="Essential",
        description="Essential to operating the service or product, including legal obligations, support and basic system operations.",
        organization_fides_key="default_organization",
        parent_key=None,
        is_default=True,
    ),
    DataUse(
        fides_key="essential.fraud_detection",
        organization_fides_key="default_organization",
        name="Essential Fraud Detection",
        description="Essential to detect possible fraud or misuse of the product, service, application or system.",
        parent_key="essential",
        is_default=True,
    ),
    DataUse(
        fides_key="essential.legal_obligation",
        organization_fides_key="default_organization",
        name="Essential Legal Obligation",
        description="Essential to meeting a legal or compliance obligation such as consent management.",
        parent_key="essential",
        is_default=True,
    ),
    DataUse(
        fides_key="essential.service",
        organization_fides_key="default_organization",
        name="Essential for Service",
        description="Essential to providing the product, service, application or system, without which the product/service would not be possible.",
        parent_key="essential",
        is_default=True,
    ),
    DataUse(
        fides_key="essential.service.notifications",
        organization_fides_key="default_organization",
        name="Essential Service Notifications",
        description="Essential to send notifications about the product, service, application or system.",
        parent_key="essential.service",
        is_default=True,
    ),
    DataUse(
        fides_key="essential.service.notifications.email",
        organization_fides_key="default_organization",
        name="Essential Email Service Notifications",
        description="Essential to send email notifications about the product, service, application or system.",
        parent_key="essential.service.notifications",
        is_default=True,
    ),
    DataUse(
        fides_key="essential.service.notifications.sms",
        organization_fides_key="default_organization",
        name="Essential SMS Service Notifications",
        description="Essential to send SMS notifications about the product, service, application or system.",
        parent_key="essential.service.notifications",
        is_default=True,
    ),
    DataUse(
        fides_key="essential.service.operations",
        organization_fides_key="default_organization",
        name="Essential for Service Operations",
        description="Essential to ensure the operation of the product, service, application or system.",
        parent_key="essential.service",
        is_default=True,
    ),
    DataUse(
        fides_key="essential.service.operations.support",
        organization_fides_key="default_organization",
        name="Essential for Serivce Operations Support",
        description="Essential to provide support for the product, service, application or system.",
        parent_key="essential.service.operations",
        is_default=True,
    ),
    DataUse(
        fides_key="essential.service.operations.support.optimization",
        name="Essential for Serivce Support Optimization",
        description="Essential to optimize and improve support for for the product, service, application or system.",
        parent_key="essential.service.operations.support",
        organization_fides_key="default_organization",
        is_default=True,
    ),
    DataUse(
        fides_key="essential.service.payment_processing",
        name="Essential for Service Payment Processing",
        description="Essential to process payments for the product, service, application or system.",
        parent_key="essential.service",
        organization_fides_key="default_organization",
        is_default=True,
    ),
    DataUse(
        fides_key="essential.service.upgrades",
        name="Essential for Service Upgrades",
        description="Essential to provide timely system upgrade information options.",
        parent_key="essential.service",
        organization_fides_key="default_organization",
        is_default=True,
    ),
    # Finance
    DataUse(
        fides_key="finance",
        name="Finance",
        organization_fides_key="default_organization",
        description="Finance and accounting activities such as audits and tax reporting.",
        parent_key=None,
        is_default=True,
    ),
    # Improve
    DataUse(
        fides_key="improve",
        organization_fides_key="default_organization",
        name="Improve the product, service, application or system.",
        description="Improve the product, service, application or system.",
        parent_key=None,
        is_default=True,
    ),
    DataUse(
        fides_key="improve.system",
        organization_fides_key="default_organization",
        name="System",
        description="Improve the specific product, service, application or system.",
        parent_key="improve",
        is_default=True,
    ),
    # Marketing
    DataUse(
        fides_key="marketing",
        organization_fides_key="default_organization",
        name="Marketing",
        description="Marketing, promotion, advertising and sales activities for the product, service, application or system.",
        parent_key=None,
        is_default=True,
    ),
    DataUse(
        fides_key="marketing.advertising",
        organization_fides_key="default_organization",
        name="Advertising, Marketing or Promotion",
        description="Advertising and promotion for the product, service, application or system and associated services.",
        parent_key="marketing",
        is_default=True,
    ),
    DataUse(
        fides_key="marketing.advertising.first_party",
        organization_fides_key="default_organization",
        name="First Party Advertising",
        description="Advertising and promotion based on first party data collected or derived about the user.",
        parent_key="marketing.advertising",
        is_default=True,
    ),
    DataUse(
        fides_key="marketing.advertising.first_party.contextual",
        organization_fides_key="default_organization",
        name="First Party Contextual Advertising",
        description="Contextual advertising based on current content being viewed by the user of the system or service.",
        parent_key="marketing.advertising.first_party",
        is_default=True,
    ),
    DataUse(
        fides_key="marketing.advertising.first_party.targeted",
        organization_fides_key="default_organization",
        name="First Party Personalized Advertising",
        description="Targeted advertising and promotion of services to users based on data collected, or derived about the user from use of the system.",
        parent_key="marketing.advertising.first_party",
        is_default=True,
    ),
    DataUse(
        fides_key="marketing.advertising.frequency_capping",
        name="Frequency Capping",
        description="Restricting the number of times a specific advertisement is shown to an individual.",
        parent_key="marketing.advertising",
        organization_fides_key="default_organization",
        is_default=True,
    ),
    DataUse(
        fides_key="marketing.advertising.negative_targeting",
        name="Negative Targeting",
        description="Rules used to ensure a certain audience or group is not targeted by advertising.",
        parent_key="marketing.advertising",
        organization_fides_key="default_organization",
        is_default=True,
    ),
    DataUse(
        fides_key="marketing.advertising.third_party",
        organization_fides_key="default_organization",
        name="Third Party Advertising",
        description="Advertising and promotion of services to users from data joined with or provided by 3rd parties.",
        parent_key="marketing.advertising",
        is_default=True,
    ),
    DataUse(
        fides_key="marketing.advertising.third_party.targeted",
        organization_fides_key="default_organization",
        name="Third Party Targeted Advertising",
        description="Targeted advertising and promotion of services to users from data joined with or provided by 3rd parties.",
        parent_key="marketing.advertising.third_party",
        is_default=True,
    ),
    DataUse(
        fides_key="marketing.communications",
        organization_fides_key="default_organization",
        name="Marketing Communications",
        description="Combined use of channels to message and market to a customer, user or prospect.",
        parent_key="marketing",
        is_default=True,
    ),
    DataUse(
        fides_key="marketing.communications.email",
        organization_fides_key="default_organization",
        name="Marketing Email Communications",
        description="E-mail marketing communications.",
        parent_key="marketing.communications",
        is_default=True,
    ),
    DataUse(
        fides_key="marketing.communications.sms",
        organization_fides_key="default_organization",
        name="Marketing SMS Communications",
        description="SMS marketing communications.",
        parent_key="marketing.communications",
        is_default=True,
    ),
    # Operations
    DataUse(
        fides_key="operations",
        name="Operations",
        organization_fides_key="default_organization",
        description="Business processes necessary to the organization's operation.",
        parent_key=None,
        is_default=True,
    ),
    # Personalize
    DataUse(
        fides_key="personalize",
        organization_fides_key="default_organization",
        name="Personalize",
        description="The use of specified data categories to personalize the product, service, application or system.",
        parent_key=None,
        is_default=True,
    ),
    DataUse(
        fides_key="personalize.content",
        organization_fides_key="default_organization",
        name="Content Personalization",
        description="Personalization of the content of the product, service, application or system.",
        parent_key="personalize",
        is_default=True,
    ),
    DataUse(
        fides_key="personalize.system",
        organization_fides_key="default_organization",
        name="System Personalization",
        description="Personalization of the product, service, application or system.",
        parent_key="personalize",
        is_default=True,
    ),
    #  Sales
    DataUse(
        fides_key="sales",
        name="Sales",
        organization_fides_key="default_organization",
        description="Sales activities such as communications and outreach.",
        parent_key=None,
        is_default=True,
    ),
    # Third-Party Sharing
    DataUse(
        fides_key="third_party_sharing",
        organization_fides_key="default_organization",
        name="Third Party Sharing",
        description="The transfer of data to third parties outside of the system or service's scope.",
        parent_key=None,
        is_default=True,
    ),
    DataUse(
        fides_key="third_party_sharing.legal_obligation",
        organization_fides_key="default_organization",
        name="Sharing for Legal Obligation",
        description="Sharing of data for legal obligations, including contracts, applicable laws or regulations.",
        parent_key="third_party_sharing",
        is_default=True,
    ),
    # Train AI System
    DataUse(
        fides_key="train_ai_system",
        organization_fides_key="default_organization",
        name="Train AI System",
        description="Training an AI system or data model for machine learning.",
        parent_key=None,
        is_default=True,
    ),
]
