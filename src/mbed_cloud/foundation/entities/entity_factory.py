"""
Foundation Entity Factory
=========================

The Entity Factory returns new instance of Foundation Entities using the shared SDK context. All Entities can be created
from :class:`EntityFactory` class using the following methods:

- :meth:`EntityFactory.account`
- :meth:`EntityFactory.active_session`
- :meth:`EntityFactory.api_key`
- :meth:`EntityFactory.campaign_device_metadata`
- :meth:`EntityFactory.campaign_statistics`
- :meth:`EntityFactory.campaign_statistics_events`
- :meth:`EntityFactory.certificate_enrollment`
- :meth:`EntityFactory.certificate_issuer`
- :meth:`EntityFactory.certificate_issuer_config`
- :meth:`EntityFactory.dark_theme_color`
- :meth:`EntityFactory.dark_theme_image`
- :meth:`EntityFactory.developer_certificate`
- :meth:`EntityFactory.device`
- :meth:`EntityFactory.device_enrollment`
- :meth:`EntityFactory.device_enrollment_bulk_create`
- :meth:`EntityFactory.device_enrollment_bulk_delete`
- :meth:`EntityFactory.device_enrollment_denial`
- :meth:`EntityFactory.device_events`
- :meth:`EntityFactory.device_group`
- :meth:`EntityFactory.firmware_image`
- :meth:`EntityFactory.firmware_manifest`
- :meth:`EntityFactory.identity_provider`
- :meth:`EntityFactory.identity_provider_public_key`
- :meth:`EntityFactory.light_theme_color`
- :meth:`EntityFactory.light_theme_image`
- :meth:`EntityFactory.login_history`
- :meth:`EntityFactory.login_profile`
- :meth:`EntityFactory.oidc_request`
- :meth:`EntityFactory.oidc_request_claim_mapping`
- :meth:`EntityFactory.parent_account`
- :meth:`EntityFactory.password_policy`
- :meth:`EntityFactory.policy`
- :meth:`EntityFactory.policy_group`
- :meth:`EntityFactory.pre_shared_key`
- :meth:`EntityFactory.saml2_request`
- :meth:`EntityFactory.server_credentials`
- :meth:`EntityFactory.subtenant_api_key`
- :meth:`EntityFactory.subtenant_dark_theme_color`
- :meth:`EntityFactory.subtenant_dark_theme_image`
- :meth:`EntityFactory.subtenant_identity_provider`
- :meth:`EntityFactory.subtenant_light_theme_color`
- :meth:`EntityFactory.subtenant_light_theme_image`
- :meth:`EntityFactory.subtenant_policy_group`
- :meth:`EntityFactory.subtenant_trusted_certificate`
- :meth:`EntityFactory.subtenant_user`
- :meth:`EntityFactory.subtenant_user_invitation`
- :meth:`EntityFactory.trusted_certificate`
- :meth:`EntityFactory.update_campaign`
- :meth:`EntityFactory.user`
- :meth:`EntityFactory.user_invitation`
- :meth:`EntityFactory.verification_response`

"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import object


class EntityFactory:
    """Creates instances of Foundation Entities using the shared SDK context."""

    def __init__(self, client):
        """EntityFactory takes a client to attach to the models it creates"""
        self._client = client

    def account(
        self,
        address_line1=None,
        address_line2=None,
        admin_email=None,
        admin_full_name=None,
        admin_id=None,
        admin_key=None,
        admin_name=None,
        admin_password=None,
        aliases=None,
        business_model=None,
        business_model_history=None,
        city=None,
        company=None,
        contact=None,
        contract_number=None,
        country=None,
        created_at=None,
        custom_fields=None,
        customer_number=None,
        display_name=None,
        email=None,
        end_market=None,
        expiration=None,
        expiration_warning_threshold=None,
        id=None,
        idle_timeout=None,
        limitations=None,
        limits=None,
        mfa_status=None,
        notification_emails=None,
        parent_account=None,
        parent_id=None,
        password_policy=None,
        password_recovery_expiration=None,
        phone_number=None,
        policies=None,
        postal_code=None,
        reason=None,
        reference_note=None,
        sales_contact=None,
        state=None,
        status=None,
        template_id=None,
        tier=None,
        tier_history=None,
        updated_at=None,
        upgraded_at=None,
    ):
        """Creates a local `Account` instance, using the shared SDK context.

        :param address_line1: Postal address line 1.
        :type address_line1: str
        :param address_line2: Postal address line 2.
        :type address_line2: str
        :param admin_email: The email address of the admin user created for this account.
            Present only in the response for account creation.
        :type admin_email: str
        :param admin_full_name: The full name of the admin user created for this account. Present
            only in the response for account creation.
        :type admin_full_name: str
        :param admin_id: The ID of the admin user created for this account. Present only in
            the response for the account creation.
        :type admin_id: str
        :param admin_key: The admin API key created for this account. Present only in the
            response for account creation.
        :type admin_key: str
        :param admin_name: The username of the admin user created for this account. Present
            only in the response for account creation.
        :type admin_name: str
        :param admin_password: The password of the admin user created for this account. Present
            only in the response for account creation.
        :type admin_password: str
        :param aliases: An array of aliases.
        :type aliases: list
        :param business_model: Business model for this account. Manageable by the root admin
            only.
        :type business_model: str
        :param business_model_history: Business model history for this account.
        :type business_model_history: list
        :param city: The city part of the postal address.
        :type city: str
        :param company: The name of the company.
        :type company: str
        :param contact: The name of the contact person for this account.
        :type contact: str
        :param contract_number: Contract number of the customer.
        :type contract_number: str
        :param country: The country part of the postal address.
        :type country: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param custom_fields: Account's custom properties as key-value pairs.
        :type custom_fields: dict
        :param customer_number: Customer number of the customer.
        :type customer_number: str
        :param display_name: The display name for the account.
        :type display_name: str
        :param email: The company email address for this account.
        :type email: str
        :param end_market: Account end market.
        :type end_market: str
        :param expiration: Expiration time of the account, as UTC time RFC3339.
        :type expiration: datetime
        :param expiration_warning_threshold: Indicates how many days (1-180) before account expiration a
            notification email is sent.
        :type expiration_warning_threshold: int
        :param id: Account ID.
        :type id: str
        :param idle_timeout: The reference token expiration time, in minutes, for this account.
        :type idle_timeout: int
        :param limitations: List of account limitation objects.
        :type limitations: list
        :param limits: List of limits as key-value pairs if requested.
        :type limits: dict
        :param mfa_status: The enforcement status of multi-factor authentication, either
            `enforced` or `optional`.
        :type mfa_status: str
        :param notification_emails: A list of notification email addresses.
        :type notification_emails: list
        :param parent_account: Represents parent account contact details in responses.
        :type parent_account: dict
        :param parent_id: The ID of the parent account, if any.
        :type parent_id: str
        :param password_policy: The password policy for this account.
        :type password_policy: dict
        :param password_recovery_expiration: Indicates for how many minutes a password recovery email is valid.
        :type password_recovery_expiration: int
        :param phone_number: The phone number of a company representative.
        :type phone_number: str
        :param policies: List of policies if requested.
        :type policies: list
        :param postal_code: The postal code part of the postal address.
        :type postal_code: str
        :param reason: A note with the reason for account status update.
        :type reason: str
        :param reference_note: A reference note for updating the status of the account.
        :type reference_note: str
        :param sales_contact: Email address of the sales contact.
        :type sales_contact: str
        :param state: The state part of the postal address.
        :type state: str
        :param status: The status of the account.
        :type status: str
        :param template_id: Account template ID.
        :type template_id: str
        :param tier: The tier level of the account; `0`: free tier, `1`: commercial
            account, `2`: partner tier. Other values are reserved for the
            future.
        :type tier: str
        :param tier_history: Tier history for this account.
        :type tier_history: list
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param upgraded_at: Time when upgraded to commercial account in UTC format RFC3339.
        :type upgraded_at: datetime
        
        :return: A new instance of a Account Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.account.Account
        """
        from mbed_cloud.foundation import Account

        return Account(
            _client=self._client,
            address_line1=address_line1,
            address_line2=address_line2,
            admin_email=admin_email,
            admin_full_name=admin_full_name,
            admin_id=admin_id,
            admin_key=admin_key,
            admin_name=admin_name,
            admin_password=admin_password,
            aliases=aliases,
            business_model=business_model,
            business_model_history=business_model_history,
            city=city,
            company=company,
            contact=contact,
            contract_number=contract_number,
            country=country,
            created_at=created_at,
            custom_fields=custom_fields,
            customer_number=customer_number,
            display_name=display_name,
            email=email,
            end_market=end_market,
            expiration=expiration,
            expiration_warning_threshold=expiration_warning_threshold,
            id=id,
            idle_timeout=idle_timeout,
            limitations=limitations,
            limits=limits,
            mfa_status=mfa_status,
            notification_emails=notification_emails,
            parent_account=parent_account,
            parent_id=parent_id,
            password_policy=password_policy,
            password_recovery_expiration=password_recovery_expiration,
            phone_number=phone_number,
            policies=policies,
            postal_code=postal_code,
            reason=reason,
            reference_note=reference_note,
            sales_contact=sales_contact,
            state=state,
            status=status,
            template_id=template_id,
            tier=tier,
            tier_history=tier_history,
            updated_at=updated_at,
            upgraded_at=upgraded_at,
        )

    def active_session(
        self, account_id=None, created_at=None, ip_address=None, login_time=None, reference_token=None, user_agent=None,
    ):
        """Creates a local `ActiveSession` instance, using the shared SDK context.

        :param account_id: The UUID of the account.
        :type account_id: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param ip_address: IP address of the client.
        :type ip_address: str
        :param login_time: The login time of the user.
        :type login_time: datetime
        :param reference_token: The reference token.
        :type reference_token: str
        :param user_agent: User Agent header from the login request.
        :type user_agent: str
        
        :return: A new instance of a ActiveSession Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.active_session.ActiveSession
        """
        from mbed_cloud.foundation import ActiveSession

        return ActiveSession(
            _client=self._client,
            account_id=account_id,
            created_at=created_at,
            ip_address=ip_address,
            login_time=login_time,
            reference_token=reference_token,
            user_agent=user_agent,
        )

    def api_key(
        self,
        account_id=None,
        created_at=None,
        creation_time=None,
        groups=None,
        id=None,
        key=None,
        last_login_time=None,
        name=None,
        owner=None,
        status=None,
        updated_at=None,
    ):
        """Creates a local `ApiKey` instance, using the shared SDK context.

        :param account_id: The ID of the account.
        :type account_id: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param creation_time: The timestamp of the API key creation in the storage, in
            milliseconds.
        :type creation_time: int
        :param groups: A list of group IDs this API key belongs to.
        :type groups: list
        :param id: The ID of the API key.
        :type id: str
        :param key: The API key.
        :type key: str
        :param last_login_time: The timestamp of the latest API key usage, in milliseconds.
        :type last_login_time: int
        :param name: The display name for the API key.
        :type name: str
        :param owner: The owner of this API key, who is the creator by default.
        :type owner: str
        :param status: The status of the API key.
        :type status: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        
        :return: A new instance of a ApiKey Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.api_key.ApiKey
        """
        from mbed_cloud.foundation import ApiKey

        return ApiKey(
            _client=self._client,
            account_id=account_id,
            created_at=created_at,
            creation_time=creation_time,
            groups=groups,
            id=id,
            key=key,
            last_login_time=last_login_time,
            name=name,
            owner=owner,
            status=status,
            updated_at=updated_at,
        )

    def campaign_device_metadata(
        self,
        campaign_id=None,
        created_at=None,
        deployment_state=None,
        description=None,
        device_id=None,
        id=None,
        mechanism=None,
        mechanism_url=None,
        name=None,
        updated_at=None,
    ):
        """Creates a local `CampaignDeviceMetadata` instance, using the shared SDK context.

        :param campaign_id: The device's campaign ID.
        :type campaign_id: str
        :param created_at: The time the entity was created.
        :type created_at: datetime
        :param deployment_state: The state of the update campaign on the device.
        :type deployment_state: str
        :param description: Description.
        :type description: str
        :param device_id: The device ID.
        :type device_id: str
        :param id: The metadata record ID.
        :type id: str
        :param mechanism: How the firmware is delivered (connector or direct).
        :type mechanism: str
        :param mechanism_url: The Device Management Connect URL.
        :type mechanism_url: str
        :param name: The record name.
        :type name: str
        :param updated_at: The time the entity was updated.
        :type updated_at: datetime
        
        :return: A new instance of a CampaignDeviceMetadata Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.device_update.campaign_device_metadata.CampaignDeviceMetadata
        """
        from mbed_cloud.foundation import CampaignDeviceMetadata

        return CampaignDeviceMetadata(
            _client=self._client,
            campaign_id=campaign_id,
            created_at=created_at,
            deployment_state=deployment_state,
            description=description,
            device_id=device_id,
            id=id,
            mechanism=mechanism,
            mechanism_url=mechanism_url,
            name=name,
            updated_at=updated_at,
        )

    def campaign_statistics(
        self, campaign_id=None, count=None, created_at=None, id=None, summary_status=None,
    ):
        """Creates a local `CampaignStatistics` instance, using the shared SDK context.

        :param campaign_id: ID of the associated campaign.
        :type campaign_id: str
        :param count: 
        :type count: int
        :param created_at: 
        :type created_at: datetime
        :param id: ID of the event type description.
        :type id: str
        :param summary_status: The event type description.
        :type summary_status: str
        
        :return: A new instance of a CampaignStatistics Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.device_update.campaign_statistics.CampaignStatistics
        """
        from mbed_cloud.foundation import CampaignStatistics

        return CampaignStatistics(
            _client=self._client,
            campaign_id=campaign_id,
            count=count,
            created_at=created_at,
            id=id,
            summary_status=summary_status,
        )

    def campaign_statistics_events(
        self,
        campaign_id=None,
        count=None,
        created_at=None,
        description=None,
        event_type=None,
        id=None,
        summary_status=None,
        summary_status_id=None,
    ):
        """Creates a local `CampaignStatisticsEvents` instance, using the shared SDK context.

        :param campaign_id: ID of the associated campaign.
        :type campaign_id: str
        :param count: 
        :type count: int
        :param created_at: 
        :type created_at: datetime
        :param description: 
        :type description: str
        :param event_type: 
        :type event_type: str
        :param id: 
        :type id: str
        :param summary_status: 
        :type summary_status: str
        :param summary_status_id: 
        :type summary_status_id: str
        
        :return: A new instance of a CampaignStatisticsEvents Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.device_update.campaign_statistics_events.CampaignStatisticsEvents
        """
        from mbed_cloud.foundation import CampaignStatisticsEvents

        return CampaignStatisticsEvents(
            _client=self._client,
            campaign_id=campaign_id,
            count=count,
            created_at=created_at,
            description=description,
            event_type=event_type,
            id=id,
            summary_status=summary_status,
            summary_status_id=summary_status_id,
        )

    def certificate_enrollment(
        self,
        certificate_name=None,
        created_at=None,
        device_id=None,
        enroll_result=None,
        enroll_result_detail=None,
        enroll_status=None,
        id=None,
        updated_at=None,
    ):
        """Creates a local `CertificateEnrollment` instance, using the shared SDK context.

        :param certificate_name: The certificate name.
        :type certificate_name: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param device_id: The device ID.
        :type device_id: str
        :param enroll_result: The result of certificate enrollment request.
        :type enroll_result: str
        :param enroll_result_detail: Additional information in case of failure.
        :type enroll_result_detail: str
        :param enroll_status: The status of certificate enrollment request.
        :type enroll_status: str
        :param id: The certificate enrollment ID.
        :type id: str
        :param updated_at: Update UTC time RFC3339.
        :type updated_at: datetime
        
        :return: A new instance of a CertificateEnrollment Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.security.certificate_enrollment.CertificateEnrollment
        """
        from mbed_cloud.foundation import CertificateEnrollment

        return CertificateEnrollment(
            _client=self._client,
            certificate_name=certificate_name,
            created_at=created_at,
            device_id=device_id,
            enroll_result=enroll_result,
            enroll_result_detail=enroll_result_detail,
            enroll_status=enroll_status,
            id=id,
            updated_at=updated_at,
        )

    def certificate_issuer(
        self, created_at=None, description=None, id=None, issuer_attributes=None, issuer_type=None, name=None,
    ):
        """Creates a local `CertificateIssuer` instance, using the shared SDK context.

        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param description: General description for the certificate issuer.
        :type description: str
        :param id: The ID of the certificate issuer.
        :type id: str
        :param issuer_attributes: General attributes for connecting the certificate issuer.
            When the issuer_type is GLOBAL_SIGN, the value shall be empty.
            When the issuer_type is CFSSL_AUTH, see definition of
            CfsslAttributes.
        :type issuer_attributes: dict
        :param issuer_type: The type of the certificate issuer.
            - GLOBAL_SIGN:
              Certificates are issued by GlobalSign service. The users must
            provide their own GlobalSign account credentials.
            - CFSSL_AUTH:
              Certificates are issued by CFSSL authenticated signing service.
              The users must provide their own CFSSL host_url and credentials.
        :type issuer_type: str
        :param name: Certificate issuer name, unique per account.
        :type name: str
        
        :return: A new instance of a CertificateIssuer Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.security.certificate_issuer.CertificateIssuer
        """
        from mbed_cloud.foundation import CertificateIssuer

        return CertificateIssuer(
            _client=self._client,
            created_at=created_at,
            description=description,
            id=id,
            issuer_attributes=issuer_attributes,
            issuer_type=issuer_type,
            name=name,
        )

    def certificate_issuer_config(
        self, certificate_issuer_id=None, created_at=None, id=None, reference=None, updated_at=None,
    ):
        """Creates a local `CertificateIssuerConfig` instance, using the shared SDK context.

        :param certificate_issuer_id: The ID of the certificate issuer.
            Null if Device Management internal HSM is used.
        :type certificate_issuer_id: str
        :param created_at: Created UTC time RFC3339.
        :type created_at: datetime
        :param id: The ID of the certificate issuer configuration.
        :type id: str
        :param reference: The certificate name to which the certificate issuer configuration
            applies.
        :type reference: str
        :param updated_at: Updated UTC time RFC3339.
        :type updated_at: datetime
        
        :return: A new instance of a CertificateIssuerConfig Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.security.certificate_issuer_config.CertificateIssuerConfig
        """
        from mbed_cloud.foundation import CertificateIssuerConfig

        return CertificateIssuerConfig(
            _client=self._client,
            certificate_issuer_id=certificate_issuer_id,
            created_at=created_at,
            id=id,
            reference=reference,
            updated_at=updated_at,
        )

    def dark_theme_color(
        self, color=None, reference=None, updated_at=None,
    ):
        """Creates a local `DarkThemeColor` instance, using the shared SDK context.

        :param color: The color given as name (purple) or as a hex code.
        :type color: str
        :param reference: Color name.
        :type reference: str
        :param updated_at: Last update time in UTC.
        :type updated_at: datetime
        
        :return: A new instance of a DarkThemeColor Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.branding.dark_theme_color.DarkThemeColor
        """
        from mbed_cloud.foundation import DarkThemeColor

        return DarkThemeColor(_client=self._client, color=color, reference=reference, updated_at=updated_at,)

    def dark_theme_image(
        self, reference=None, static_uri=None, updated_at=None,
    ):
        """Creates a local `DarkThemeImage` instance, using the shared SDK context.

        :param reference: Name of the image.
        :type reference: str
        :param static_uri: The static link to the image.
        :type static_uri: str
        :param updated_at: Last update time in UTC.
        :type updated_at: datetime
        
        :return: A new instance of a DarkThemeImage Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.branding.dark_theme_image.DarkThemeImage
        """
        from mbed_cloud.foundation import DarkThemeImage

        return DarkThemeImage(_client=self._client, reference=reference, static_uri=static_uri, updated_at=updated_at,)

    def developer_certificate(
        self,
        account_id=None,
        certificate=None,
        created_at=None,
        description=None,
        developer_private_key=None,
        id=None,
        name=None,
        security_file_content=None,
    ):
        """Creates a local `DeveloperCertificate` instance, using the shared SDK context.

        :param account_id: Account to which the developer certificate belongs.
        :type account_id: str
        :param certificate: PEM-format X.509 developer certificate.
        :type certificate: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param description: Description for the developer certificate.
        :type description: str
        :param developer_private_key: PEM-format developer private key associated with the certificate.
        :type developer_private_key: str
        :param id: ID that uniquely identifies the developer certificate.
        :type id: str
        :param name: Name of the developer certificate.
        :type name: str
        :param security_file_content: Content of the `security.c` file flashed to the device to provide
            security credentials.
        :type security_file_content: str
        
        :return: A new instance of a DeveloperCertificate Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.security.developer_certificate.DeveloperCertificate
        """
        from mbed_cloud.foundation import DeveloperCertificate

        return DeveloperCertificate(
            _client=self._client,
            account_id=account_id,
            certificate=certificate,
            created_at=created_at,
            description=description,
            developer_private_key=developer_private_key,
            id=id,
            name=name,
            security_file_content=security_file_content,
        )

    def device(
        self,
        account_id=None,
        auto_update=None,
        bootstrap_expiration_date=None,
        bootstrapped_timestamp=None,
        ca_id=None,
        connector_expiration_date=None,
        created_at=None,
        custom_attributes=None,
        deployed_state=None,
        deployment=None,
        description=None,
        device_class=None,
        device_execution_mode=None,
        device_key=None,
        endpoint_name=None,
        endpoint_type=None,
        enrolment_list_timestamp=None,
        firmware_checksum=None,
        groups=None,
        host_gateway=None,
        id=None,
        issuer_fingerprint=None,
        last_operator_suspended_category=None,
        last_operator_suspended_description=None,
        last_operator_suspended_updated_at=None,
        last_system_suspended_category=None,
        last_system_suspended_description=None,
        last_system_suspended_updated_at=None,
        lifecycle_status=None,
        manifest=None,
        manifest_timestamp=None,
        mechanism=None,
        mechanism_url=None,
        name=None,
        operator_suspended=None,
        serial_number=None,
        state=None,
        system_suspended=None,
        updated_at=None,
        vendor_id=None,
    ):
        """Creates a local `Device` instance, using the shared SDK context.

        :param account_id: The ID of the associated account.
        :type account_id: str
        :param auto_update: DEPRECATED: Mark this device for automatic firmware update.
        :type auto_update: bool
        :param bootstrap_expiration_date: The expiration date of the certificate used to connect to
            bootstrap server.
        :type bootstrap_expiration_date: date
        :param bootstrapped_timestamp: The timestamp of the device's most recent bootstrap process.
        :type bootstrapped_timestamp: datetime
        :param ca_id: The certificate issuer's ID.
        :type ca_id: str
        :param connector_expiration_date: The expiration date of the certificate used to connect to LwM2M
            server.
        :type connector_expiration_date: date
        :param created_at: The timestamp of when the device was created in the device
            directory.
        :type created_at: datetime
        :param custom_attributes: Up to five custom key-value attributes. Note that keys cannot
            begin with a number. Both keys and values are limited to 128
            characters. Updating this field replaces existing contents.
        :type custom_attributes: dict
        :param deployed_state: DEPRECATED: The state of the device's deployment.
        :type deployed_state: str
        :param deployment: DEPRECATED: The last deployment used on the device.
        :type deployment: str
        :param description: The description of the device.
        :type description: str
        :param device_class: An ID representing the model and hardware revision of the device.
        :type device_class: str
        :param device_execution_mode: The execution mode from the certificate of the device. Defaults to
            inheriting from host_gateway device.
            Permitted values:
              - 0 - Unspecified execution mode (default if host_gateway
            invalid or not set). The device firmware uses a certificate that
            is not identified as a developer or production certificate.
              - 1 - Development device. The device firmware uses a developer
            certificate to communicate with Device Management.
              - 5 - Production device. The device firmware uses a factory-
            generated certificate to communicate with Device Management.
        :type device_execution_mode: int
        :param device_key: The fingerprint of the device certificate.
        :type device_key: str
        :param endpoint_name: The endpoint name given to the device. The endpoint_name is from
            the device certificate and is set by factory tool.
        :type endpoint_name: str
        :param endpoint_type: The endpoint type of the device. For example, the device is a
            gateway.
        :type endpoint_type: str
        :param enrolment_list_timestamp: The claim date/time.
        :type enrolment_list_timestamp: datetime
        :param firmware_checksum: The SHA256 checksum of the current firmware image.
        :type firmware_checksum: str
        :param groups: An array containing an ID of each group this device belongs to.
        :type groups: list
        :param host_gateway: The ID of the host gateway, if appropriate. A device behind Edge
            has this host_gateway set.
        :type host_gateway: str
        :param id: The ID of the device. The device ID is used across all Device
            Management APIs.
        :type id: str
        :param issuer_fingerprint: SHA256 fingerprint of the certificate used to validate the
            signature of the device certificate.
        :type issuer_fingerprint: str
        :param last_operator_suspended_category: The reference of the block category.
        :type last_operator_suspended_category: str
        :param last_operator_suspended_description: The most recent description why the device was suspended or
            returned to service.
        :type last_operator_suspended_description: str
        :param last_operator_suspended_updated_at: The timestamp of the most recent suspension activity.
        :type last_operator_suspended_updated_at: datetime
        :param last_system_suspended_category: The reference of the block category.
        :type last_system_suspended_category: str
        :param last_system_suspended_description: The most recent description of why the device was blocked or
            unblocked by the system.
        :type last_system_suspended_description: str
        :param last_system_suspended_updated_at: The timestamp of the most recent system block activity.
        :type last_system_suspended_updated_at: datetime
        :param lifecycle_status: The lifecycle status of the device.
            * Enabled: The device is allowed to connect to Pelion Device
            Management.
            * Blocked: The device is prevented from connecting to Pelion
            Device Management. Device can be, for example, 'suspended'.
        :type lifecycle_status: str
        :param manifest: DEPRECATED: The URL for the current device manifest.
        :type manifest: str
        :param manifest_timestamp: The timestamp of the current manifest version.
        :type manifest_timestamp: datetime
        :param mechanism: NOT USED: The ID of the channel used to communicate with the
            device.
        :type mechanism: str
        :param mechanism_url: NOT USED: The address of the connector to use.
        :type mechanism_url: str
        :param name: The name given by the web application for the device. Device
            itself provides only the endpoint_name.
        :type name: str
        :param operator_suspended: Device has been suspended by operator.
        :type operator_suspended: bool
        :param serial_number: The [serial number](../provisioning-process/provisioning-
            information.html#serial-number) of the device. The serial number
            is injected by the factory tool during manufacturing.
        :type serial_number: str
        :param state: The current state of the device.
            * Unenrolled: The device has been created, but has not yet
            bootstrapped or connected to Device Management.
            * Cloud_enrolling: The device is bootstrapping for the first time.
            This state is set only while bootstrapping is in progress. For
            example, an external CA gives an error, and the device tries to
            bootstrap again after few seconds.
            * Bootstrapped: The device has bootstrapped, and has credentials
            to connect to Device Management.
            * Registered: The device has registered with Pelion Device
            Management. [Device commands](../service-api-references/device-
            management-connect.html#createAsyncRequest) can be queued. The
            device sends events for [subscribed](../connecting/resource-
            change-webapp.html) resources.
            * Deregistered: The device has requested deregistration, or its
            registration has expired.
        :type state: str
        :param system_suspended: Is the device suspended by the system?
        :type system_suspended: bool
        :param updated_at: The time this data object was updated.
        :type updated_at: datetime
        :param vendor_id: The device vendor ID.
        :type vendor_id: str
        
        :return: A new instance of a Device Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.devices.device.Device
        """
        from mbed_cloud.foundation import Device

        return Device(
            _client=self._client,
            account_id=account_id,
            auto_update=auto_update,
            bootstrap_expiration_date=bootstrap_expiration_date,
            bootstrapped_timestamp=bootstrapped_timestamp,
            ca_id=ca_id,
            connector_expiration_date=connector_expiration_date,
            created_at=created_at,
            custom_attributes=custom_attributes,
            deployed_state=deployed_state,
            deployment=deployment,
            description=description,
            device_class=device_class,
            device_execution_mode=device_execution_mode,
            device_key=device_key,
            endpoint_name=endpoint_name,
            endpoint_type=endpoint_type,
            enrolment_list_timestamp=enrolment_list_timestamp,
            firmware_checksum=firmware_checksum,
            groups=groups,
            host_gateway=host_gateway,
            id=id,
            issuer_fingerprint=issuer_fingerprint,
            last_operator_suspended_category=last_operator_suspended_category,
            last_operator_suspended_description=last_operator_suspended_description,
            last_operator_suspended_updated_at=last_operator_suspended_updated_at,
            last_system_suspended_category=last_system_suspended_category,
            last_system_suspended_description=last_system_suspended_description,
            last_system_suspended_updated_at=last_system_suspended_updated_at,
            lifecycle_status=lifecycle_status,
            manifest=manifest,
            manifest_timestamp=manifest_timestamp,
            mechanism=mechanism,
            mechanism_url=mechanism_url,
            name=name,
            operator_suspended=operator_suspended,
            serial_number=serial_number,
            state=state,
            system_suspended=system_suspended,
            updated_at=updated_at,
            vendor_id=vendor_id,
        )

    def device_enrollment(
        self,
        account_id=None,
        claimed_at=None,
        created_at=None,
        enrolled_device_id=None,
        enrollment_identity=None,
        expires_at=None,
        id=None,
    ):
        """Creates a local `DeviceEnrollment` instance, using the shared SDK context.

        :param account_id: ID
        :type account_id: str
        :param claimed_at: The time the device was claimed.
        :type claimed_at: datetime
        :param created_at: The time of the enrollment identity creation.
        :type created_at: datetime
        :param enrolled_device_id: The ID of the device in the Device Directory once it is
            registered.
        :type enrolled_device_id: str
        :param enrollment_identity: Enrollment identity.
        :type enrollment_identity: str
        :param expires_at: The enrollment claim expiration time. If the device does not
            connect to Device Management before expiration, the claim is
            removed without separate notice.
        :type expires_at: datetime
        :param id: Enrollment identity.
        :type id: str
        
        :return: A new instance of a DeviceEnrollment Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.devices.device_enrollment.DeviceEnrollment
        """
        from mbed_cloud.foundation import DeviceEnrollment

        return DeviceEnrollment(
            _client=self._client,
            account_id=account_id,
            claimed_at=claimed_at,
            created_at=created_at,
            enrolled_device_id=enrolled_device_id,
            enrollment_identity=enrollment_identity,
            expires_at=expires_at,
            id=id,
        )

    def device_enrollment_bulk_create(
        self,
        account_id=None,
        completed_at=None,
        created_at=None,
        errors_count=None,
        errors_report_file=None,
        full_report_file=None,
        id=None,
        processed_count=None,
        status=None,
        total_count=None,
    ):
        """Creates a local `DeviceEnrollmentBulkCreate` instance, using the shared SDK context.

        :param account_id: ID
        :type account_id: str
        :param completed_at: The time the bulk creation task was completed.
            Null when creating bulk upload or delete.
        :type completed_at: datetime
        :param created_at: The time of receiving the bulk creation task.
        :type created_at: datetime
        :param errors_count: The number of enrollment identities with failed processing.
        :type errors_count: int
        :param errors_report_file: Link to error report file.
            Null when creating bulk upload or delete.
        :type errors_report_file: str
        :param full_report_file: Link to full report file.
            Null when creating bulk upload or delete.
        :type full_report_file: str
        :param id: Bulk ID
        :type id: str
        :param processed_count: The number of enrollment identities processed until now.
        :type processed_count: int
        :param status: The state of the process is 'new' at the time of creation. If
            creation is still in progress, the state shows as 'processing'.
            When the request is fully processed, the state changes to
            'completed'.
        :type status: str
        :param total_count: Total number of enrollment identities found in the input CSV.
        :type total_count: int
        
        :return: A new instance of a DeviceEnrollmentBulkCreate Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.devices.device_enrollment_bulk_create.DeviceEnrollmentBulkCreate
        """
        from mbed_cloud.foundation import DeviceEnrollmentBulkCreate

        return DeviceEnrollmentBulkCreate(
            _client=self._client,
            account_id=account_id,
            completed_at=completed_at,
            created_at=created_at,
            errors_count=errors_count,
            errors_report_file=errors_report_file,
            full_report_file=full_report_file,
            id=id,
            processed_count=processed_count,
            status=status,
            total_count=total_count,
        )

    def device_enrollment_bulk_delete(
        self,
        account_id=None,
        completed_at=None,
        created_at=None,
        errors_count=None,
        errors_report_file=None,
        full_report_file=None,
        id=None,
        processed_count=None,
        status=None,
        total_count=None,
    ):
        """Creates a local `DeviceEnrollmentBulkDelete` instance, using the shared SDK context.

        :param account_id: ID
        :type account_id: str
        :param completed_at: The time the bulk creation task was completed.
            Null when creating bulk upload or delete.
        :type completed_at: datetime
        :param created_at: The time of receiving the bulk creation task.
        :type created_at: datetime
        :param errors_count: The number of enrollment identities with failed processing.
        :type errors_count: int
        :param errors_report_file: Link to error report file.
            Null when creating bulk upload or delete.
        :type errors_report_file: str
        :param full_report_file: Link to full report file.
            Null when creating bulk upload or delete.
        :type full_report_file: str
        :param id: Bulk ID
        :type id: str
        :param processed_count: The number of enrollment identities processed until now.
        :type processed_count: int
        :param status: The state of the process is 'new' at the time of creation. If
            creation is still in progress, the state shows as 'processing'.
            When the request is fully processed, the state changes to
            'completed'.
        :type status: str
        :param total_count: Total number of enrollment identities found in the input CSV.
        :type total_count: int
        
        :return: A new instance of a DeviceEnrollmentBulkDelete Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.devices.device_enrollment_bulk_delete.DeviceEnrollmentBulkDelete
        """
        from mbed_cloud.foundation import DeviceEnrollmentBulkDelete

        return DeviceEnrollmentBulkDelete(
            _client=self._client,
            account_id=account_id,
            completed_at=completed_at,
            created_at=created_at,
            errors_count=errors_count,
            errors_report_file=errors_report_file,
            full_report_file=full_report_file,
            id=id,
            processed_count=processed_count,
            status=status,
            total_count=total_count,
        )

    def device_enrollment_denial(
        self, account_id=None, created_at=None, endpoint_name=None, id=None, trusted_certificate_id=None,
    ):
        """Creates a local `DeviceEnrollmentDenial` instance, using the shared SDK context.

        :param account_id: account id
        :type account_id: str
        :param created_at: date on which the failed bootstrap was attempted on
        :type created_at: datetime
        :param endpoint_name: endpoint name
        :type endpoint_name: str
        :param id: id of the recorded failed bootstrap attempt
        :type id: str
        :param trusted_certificate_id: Trusted certificate id
        :type trusted_certificate_id: str
        
        :return: A new instance of a DeviceEnrollmentDenial Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.devices.device_enrollment_denial.DeviceEnrollmentDenial
        """
        from mbed_cloud.foundation import DeviceEnrollmentDenial

        return DeviceEnrollmentDenial(
            _client=self._client,
            account_id=account_id,
            created_at=created_at,
            endpoint_name=endpoint_name,
            id=id,
            trusted_certificate_id=trusted_certificate_id,
        )

    def device_events(
        self,
        changes=None,
        created_at=None,
        data=None,
        date_time=None,
        description=None,
        device_id=None,
        event_type=None,
        event_type_category=None,
        event_type_description=None,
        id=None,
        state_change=None,
    ):
        """Creates a local `DeviceEvents` instance, using the shared SDK context.

        :param changes: 
        :type changes: dict
        :param created_at: 
        :type created_at: datetime
        :param data: Additional data relevant to the event.
        :type data: dict
        :param date_time: 
        :type date_time: datetime
        :param description: 
        :type description: str
        :param device_id: 
        :type device_id: str
        :param event_type: Event code
        :type event_type: str
        :param event_type_category: Category code that groups the event type by a summary category.
        :type event_type_category: str
        :param event_type_description: Generic description of the event.
        :type event_type_description: str
        :param id: 
        :type id: str
        :param state_change: 
        :type state_change: bool
        
        :return: A new instance of a DeviceEvents Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.devices.device_events.DeviceEvents
        """
        from mbed_cloud.foundation import DeviceEvents

        return DeviceEvents(
            _client=self._client,
            changes=changes,
            created_at=created_at,
            data=data,
            date_time=date_time,
            description=description,
            device_id=device_id,
            event_type=event_type,
            event_type_category=event_type_category,
            event_type_description=event_type_description,
            id=id,
            state_change=state_change,
        )

    def device_group(
        self,
        created_at=None,
        custom_attributes=None,
        description=None,
        devices_count=None,
        id=None,
        name=None,
        updated_at=None,
    ):
        """Creates a local `DeviceGroup` instance, using the shared SDK context.

        :param created_at: The time the group was created.
        :type created_at: datetime
        :param custom_attributes: Up to ten custom key-value attributes. Keys cannot begin with a
            number. Both key and value are limited to 128 characters. Updating
            this field replaces existing contents.
        :type custom_attributes: dict
        :param description: The description of the group.
        :type description: str
        :param devices_count: The number of devices in this group.
        :type devices_count: int
        :param id: The group ID.
        :type id: str
        :param name: Name of the group.
        :type name: str
        :param updated_at: The time this object was updated.
        :type updated_at: datetime
        
        :return: A new instance of a DeviceGroup Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.devices.device_group.DeviceGroup
        """
        from mbed_cloud.foundation import DeviceGroup

        return DeviceGroup(
            _client=self._client,
            created_at=created_at,
            custom_attributes=custom_attributes,
            description=description,
            devices_count=devices_count,
            id=id,
            name=name,
            updated_at=updated_at,
        )

    def firmware_image(
        self,
        created_at=None,
        datafile_checksum=None,
        datafile_size=None,
        datafile_url=None,
        description=None,
        id=None,
        name=None,
        updated_at=None,
    ):
        """Creates a local `FirmwareImage` instance, using the shared SDK context.

        :param created_at: The time the entity was created.
        :type created_at: datetime
        :param datafile_checksum: The checksum (sha256) generated for the datafile.
        :type datafile_checksum: str
        :param datafile_size: The size of the datafile in bytes.
        :type datafile_size: int
        :param datafile_url: The firmware image file URL.
        :type datafile_url: str
        :param description: The description of the object.
        :type description: str
        :param id: The firmware image ID.
        :type id: str
        :param name: The firmware image name.
        :type name: str
        :param updated_at: The time the entity was updated.
        :type updated_at: datetime
        
        :return: A new instance of a FirmwareImage Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.device_update.firmware_image.FirmwareImage
        """
        from mbed_cloud.foundation import FirmwareImage

        return FirmwareImage(
            _client=self._client,
            created_at=created_at,
            datafile_checksum=datafile_checksum,
            datafile_size=datafile_size,
            datafile_url=datafile_url,
            description=description,
            id=id,
            name=name,
            updated_at=updated_at,
        )

    def firmware_manifest(
        self,
        created_at=None,
        datafile_size=None,
        datafile_url=None,
        delivered_payload_digest=None,
        delivered_payload_size=None,
        delivered_payload_type=None,
        delivered_payload_url=None,
        description=None,
        device_class=None,
        device_vendor=None,
        id=None,
        key_table_url=None,
        manifest_schema_version=None,
        name=None,
        parsed_raw_manifest=None,
        precursor_payload_digest=None,
        timestamp=None,
        update_priority=None,
        updated_at=None,
    ):
        """Creates a local `FirmwareManifest` instance, using the shared SDK context.

        :param created_at: The time the entity was created.
        :type created_at: datetime
        :param datafile_size: The size of the firmware manifest in bytes.
        :type datafile_size: int
        :param datafile_url: The URL of the ASN.1 DER-encoded firmware manifest binary.
        :type datafile_url: str
        :param delivered_payload_digest: Digest (SHA256, hex-encoded) of the payload to deliver to the
            device.
        :type delivered_payload_digest: str
        :param delivered_payload_size: The size in bytes of the payload to deliver to the device.
        :type delivered_payload_size: int
        :param delivered_payload_type: Type of the payload to deliver to the device (full or delta
            image).
        :type delivered_payload_type: str
        :param delivered_payload_url: The URL of the payload to deliver to the device.
        :type delivered_payload_url: str
        :param description: The description of the firmware manifest.
        :type description: str
        :param device_class: The device class ID.
        :type device_class: str
        :param device_vendor: The device vendor ID.
        :type device_vendor: str
        :param id: The firmware manifest ID.
        :type id: str
        :param key_table_url: The key table of pre-shared keys for devices.
        :type key_table_url: str
        :param manifest_schema_version: Version of the manifest schema (1 or 3).
        :type manifest_schema_version: str
        :param name: The name of the manifest.
        :type name: str
        :param parsed_raw_manifest: Raw manifest in JSON format, parsed from ASN.1 DER encoding.
            Fields may change. Backwards compatibility is not guaranteed.
            Recommended for debugging only.
        :type parsed_raw_manifest: dict
        :param precursor_payload_digest: Digest (SHA256, hex-encoded) of the currently installed payload.
        :type precursor_payload_digest: str
        :param timestamp: The firmware manifest version as a timestamp.
        :type timestamp: datetime
        :param update_priority: Update priority, passed to the application callback when an update
            is performed. Allows the application to make application-specific
            decisions.
        :type update_priority: int
        :param updated_at: The time the entity was updated.
        :type updated_at: datetime
        
        :return: A new instance of a FirmwareManifest Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.device_update.firmware_manifest.FirmwareManifest
        """
        from mbed_cloud.foundation import FirmwareManifest

        return FirmwareManifest(
            _client=self._client,
            created_at=created_at,
            datafile_size=datafile_size,
            datafile_url=datafile_url,
            delivered_payload_digest=delivered_payload_digest,
            delivered_payload_size=delivered_payload_size,
            delivered_payload_type=delivered_payload_type,
            delivered_payload_url=delivered_payload_url,
            description=description,
            device_class=device_class,
            device_vendor=device_vendor,
            id=id,
            key_table_url=key_table_url,
            manifest_schema_version=manifest_schema_version,
            name=name,
            parsed_raw_manifest=parsed_raw_manifest,
            precursor_payload_digest=precursor_payload_digest,
            timestamp=timestamp,
            update_priority=update_priority,
            updated_at=updated_at,
        )

    def identity_provider(
        self,
        account_id=None,
        created_at=None,
        description=None,
        id=None,
        identity_provider_type=None,
        is_default=None,
        name=None,
        saml2_attributes=None,
        status=None,
        updated_at=None,
    ):
        """Creates a local `IdentityProvider` instance, using the shared SDK context.

        :param account_id: The ID of the account the identity provider belongs to.
        :type account_id: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param description: Description for the identity provider.
        :type description: str
        :param id: Entity ID.
        :type id: str
        :param identity_provider_type: Identity provider type.
        :type identity_provider_type: str
        :param is_default: Flag indicating whether this is the global default identity
            provider.
        :type is_default: bool
        :param name: Name of the identity provider.
        :type name: str
        :param saml2_attributes: Represents SAML2 specific attributes in responses.
        :type saml2_attributes: dict
        :param status: Status of the identity provider.
        :type status: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        
        :return: A new instance of a IdentityProvider Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.identity_provider.IdentityProvider
        """
        from mbed_cloud.foundation import IdentityProvider

        return IdentityProvider(
            _client=self._client,
            account_id=account_id,
            created_at=created_at,
            description=description,
            id=id,
            identity_provider_type=identity_provider_type,
            is_default=is_default,
            name=name,
            saml2_attributes=saml2_attributes,
            status=status,
            updated_at=updated_at,
        )

    def identity_provider_public_key(
        self, key=None, kid=None,
    ):
        """Creates a local `IdentityProviderPublicKey` instance, using the shared SDK context.

        :param key: The public key.
        :type key: str
        :param kid: The public key ID.
        :type kid: str
        
        :return: A new instance of a IdentityProviderPublicKey Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.identity_provider_public_key.IdentityProviderPublicKey
        """
        from mbed_cloud.foundation import IdentityProviderPublicKey

        return IdentityProviderPublicKey(_client=self._client, key=key, kid=kid,)

    def light_theme_color(
        self, color=None, reference=None, updated_at=None,
    ):
        """Creates a local `LightThemeColor` instance, using the shared SDK context.

        :param color: The color given as name (purple) or as a hex code.
        :type color: str
        :param reference: Color name.
        :type reference: str
        :param updated_at: Last update time in UTC.
        :type updated_at: datetime
        
        :return: A new instance of a LightThemeColor Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.branding.light_theme_color.LightThemeColor
        """
        from mbed_cloud.foundation import LightThemeColor

        return LightThemeColor(_client=self._client, color=color, reference=reference, updated_at=updated_at,)

    def light_theme_image(
        self, reference=None, static_uri=None, updated_at=None,
    ):
        """Creates a local `LightThemeImage` instance, using the shared SDK context.

        :param reference: Name of the image.
        :type reference: str
        :param static_uri: The static link to the image.
        :type static_uri: str
        :param updated_at: Last update time in UTC.
        :type updated_at: datetime
        
        :return: A new instance of a LightThemeImage Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.branding.light_theme_image.LightThemeImage
        """
        from mbed_cloud.foundation import LightThemeImage

        return LightThemeImage(_client=self._client, reference=reference, static_uri=static_uri, updated_at=updated_at,)

    def login_history(
        self, date=None, ip_address=None, success=None, user_agent=None,
    ):
        """Creates a local `LoginHistory` instance, using the shared SDK context.

        :param date: UTC time RFC3339 for this login attempt.
        :type date: datetime
        :param ip_address: IP address of the client.
        :type ip_address: str
        :param success: Flag indicating whether login attempt was successful or not.
        :type success: bool
        :param user_agent: User Agent header from the login request.
        :type user_agent: str
        
        :return: A new instance of a LoginHistory Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.login_history.LoginHistory
        """
        from mbed_cloud.foundation import LoginHistory

        return LoginHistory(
            _client=self._client, date=date, ip_address=ip_address, success=success, user_agent=user_agent,
        )

    def login_profile(
        self, foreign_id=None, id=None, login_profile_type=None, name=None,
    ):
        """Creates a local `LoginProfile` instance, using the shared SDK context.

        :param foreign_id: The ID of the user in the identity provider's service.
        :type foreign_id: str
        :param id: ID of the identity provider.
        :type id: str
        :param login_profile_type: Identity provider type.
        :type login_profile_type: str
        :param name: Name of the identity provider.
        :type name: str
        
        :return: A new instance of a LoginProfile Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.login_profile.LoginProfile
        """
        from mbed_cloud.foundation import LoginProfile

        return LoginProfile(
            _client=self._client, foreign_id=foreign_id, id=id, login_profile_type=login_profile_type, name=name,
        )

    def oidc_request(
        self,
        authorization_endpoint=None,
        auto_enrollment=None,
        claim_mapping=None,
        client_id=None,
        client_secret=None,
        end_session_endpoint=None,
        issuer=None,
        jwks_uri=None,
        keys=None,
        redirect_uri=None,
        revocation_endpoint=None,
        scopes=None,
        token_endpoint=None,
        token_request_mode=None,
        token_response_path=None,
        userinfo_endpoint=None,
    ):
        """Creates a local `OidcRequest` instance, using the shared SDK context.

        :param authorization_endpoint: URL of the OAuth 2.0 authorization endpoint.
        :type authorization_endpoint: str
        :param auto_enrollment: For future use.
        :type auto_enrollment: bool
        :param claim_mapping: Mapping for non-standard OIDC claim names.
        :type claim_mapping: dict
        :param client_id: Client ID needed to authenticate and gain access to identity
            provider's API.
        :type client_id: str
        :param client_secret: Client secret needed to authenticate and gain access to identity
            provider's API.
        :type client_secret: str
        :param end_session_endpoint: URL of the provider's end session endpoint.
        :type end_session_endpoint: str
        :param issuer: Issuer of the identity provider.
        :type issuer: str
        :param jwks_uri: URL of the provider's JSON web key set document.
        :type jwks_uri: str
        :param keys: Provider's public keys and key IDs used to sign ID tokens. PEM-
            encoded.
        :type keys: list
        :param redirect_uri: The URI needed to authenticate and gain access to identity
            provider's API. Leave this empty to use the default redirect URI.
        :type redirect_uri: str
        :param revocation_endpoint: URL of the provider's token revocation endpoint.
        :type revocation_endpoint: str
        :param scopes: Space-separated list of scopes sent in the authentication request.
            When not configured otherwise, the default scopes are ['openid
            profile email'](https://openid.net/specs/openid-connect-
            core-1_0.html#ScopeClaims).
        :type scopes: str
        :param token_endpoint: URL of the OAuth 2.0 authorization endpoint.
        :type token_endpoint: str
        :param token_request_mode: One way to obtain the access token. Since the request results in
            the transmission of clear-text credentials, the client must use
            the POST mode.
        :type token_request_mode: str
        :param token_response_path: Path to the standard data in the token response. Levels in the
            JSON structure must be separated by '.' (dot) characters.
        :type token_response_path: str
        :param userinfo_endpoint: URL of the OAuth 2.0 UserInfo endpoint.
        :type userinfo_endpoint: str
        
        :return: A new instance of a OidcRequest Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.oidc_request.OidcRequest
        """
        from mbed_cloud.foundation import OidcRequest

        return OidcRequest(
            _client=self._client,
            authorization_endpoint=authorization_endpoint,
            auto_enrollment=auto_enrollment,
            claim_mapping=claim_mapping,
            client_id=client_id,
            client_secret=client_secret,
            end_session_endpoint=end_session_endpoint,
            issuer=issuer,
            jwks_uri=jwks_uri,
            keys=keys,
            redirect_uri=redirect_uri,
            revocation_endpoint=revocation_endpoint,
            scopes=scopes,
            token_endpoint=token_endpoint,
            token_request_mode=token_request_mode,
            token_response_path=token_response_path,
            userinfo_endpoint=userinfo_endpoint,
        )

    def oidc_request_claim_mapping(
        self,
        email=None,
        email_verified=None,
        family_name=None,
        given_name=None,
        name=None,
        phone_number=None,
        sub=None,
        updated_at=None,
        updated_at_pattern=None,
    ):
        """Creates a local `OidcRequestClaimMapping` instance, using the shared SDK context.

        :param email: Custom claim name for 'email'.
        :type email: str
        :param email_verified: Custom claim name for 'email_verified'.
        :type email_verified: str
        :param family_name: Custom claim name for 'family_name'.
        :type family_name: str
        :param given_name: Custom claim name for 'given_name'.
        :type given_name: str
        :param name: Custom claim name for 'name'.
        :type name: str
        :param phone_number: Custom claim name for 'phone_number'.
        :type phone_number: str
        :param sub: Custom claim name for 'sub'.
        :type sub: str
        :param updated_at: Custom claim name for 'updated_at'.
        :type updated_at: str
        :param updated_at_pattern: Custom pattern for claim 'updated_at' as defined by the Java
            SimpleDateFormat class.
        :type updated_at_pattern: str
        
        :return: A new instance of a OidcRequestClaimMapping Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.oidc_request_claim_mapping.OidcRequestClaimMapping
        """
        from mbed_cloud.foundation import OidcRequestClaimMapping

        return OidcRequestClaimMapping(
            _client=self._client,
            email=email,
            email_verified=email_verified,
            family_name=family_name,
            given_name=given_name,
            name=name,
            phone_number=phone_number,
            sub=sub,
            updated_at=updated_at,
            updated_at_pattern=updated_at_pattern,
        )

    def parent_account(
        self, admin_email=None, admin_name=None, id=None,
    ):
        """Creates a local `ParentAccount` instance, using the shared SDK context.

        :param admin_email: The email address of the admin user who is the contact person of
            the parent account.
        :type admin_email: str
        :param admin_name: The name of the admin user who is the contact person of the parent
            account.
        :type admin_name: str
        :param id: The ID of the parent account.
        :type id: str
        
        :return: A new instance of a ParentAccount Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.parent_account.ParentAccount
        """
        from mbed_cloud.foundation import ParentAccount

        return ParentAccount(_client=self._client, admin_email=admin_email, admin_name=admin_name, id=id,)

    def password_policy(
        self, minimum_length=None,
    ):
        """Creates a local `PasswordPolicy` instance, using the shared SDK context.

        :param minimum_length: Minimum length for the password.
        :type minimum_length: int
        
        :return: A new instance of a PasswordPolicy Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.password_policy.PasswordPolicy
        """
        from mbed_cloud.foundation import PasswordPolicy

        return PasswordPolicy(_client=self._client, minimum_length=minimum_length,)

    def policy(
        self,
        action=None,
        allow=None,
        feature=None,
        inherited=None,
        inherited_from=None,
        inherited_type=None,
        resource=None,
    ):
        """Creates a local `Policy` instance, using the shared SDK context.

        :param action: Comma-separated list of actions, empty string represents all
            actions.
        :type action: str
        :param allow: True or false controlling whether an action is allowed or not.
        :type allow: bool
        :param feature: Feature name corresponding to this policy.
        :type feature: str
        :param inherited: Flag indicating whether this feature is inherited or overwritten
            specifically.
        :type inherited: bool
        :param inherited_from: An ID indicating where this policy is inherited from.
        :type inherited_from: str
        :param inherited_type: Indicates the type of entity this policy is inherited from.
        :type inherited_type: str
        :param resource: Resource that is protected by this policy.
        :type resource: str
        
        :return: A new instance of a Policy Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.policy.Policy
        """
        from mbed_cloud.foundation import Policy

        return Policy(
            _client=self._client,
            action=action,
            allow=allow,
            feature=feature,
            inherited=inherited,
            inherited_from=inherited_from,
            inherited_type=inherited_type,
            resource=resource,
        )

    def policy_group(
        self, account_id=None, apikey_count=None, created_at=None, id=None, name=None, updated_at=None, user_count=None,
    ):
        """Creates a local `PolicyGroup` instance, using the shared SDK context.

        :param account_id: The ID of the account this group belongs to.
        :type account_id: str
        :param apikey_count: The number of API keys in this group.
        :type apikey_count: int
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param id: The ID of the group.
        :type id: str
        :param name: The name of the group.
        :type name: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param user_count: The number of users in this group.
        :type user_count: int
        
        :return: A new instance of a PolicyGroup Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.policy_group.PolicyGroup
        """
        from mbed_cloud.foundation import PolicyGroup

        return PolicyGroup(
            _client=self._client,
            account_id=account_id,
            apikey_count=apikey_count,
            created_at=created_at,
            id=id,
            name=name,
            updated_at=updated_at,
            user_count=user_count,
        )

    def pre_shared_key(
        self, created_at=None, endpoint_name=None, id=None,
    ):
        """Creates a local `PreSharedKey` instance, using the shared SDK context.

        :param created_at: The date-time (RFC3339) when this PSK was uploaded to Device
            Management.
        :type created_at: datetime
        :param endpoint_name: The unique endpoint identifier that this PSK applies to. 16-64 [pr
            intable](https://en.wikipedia.org/wiki/ASCII#Printable_characters)
            (non-control) ASCII characters.
        :type endpoint_name: str
        :param id: The Id of the pre_shared_key, shadows the endpoint_name
        :type id: str
        
        :return: A new instance of a PreSharedKey Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.security.pre_shared_key.PreSharedKey
        """
        from mbed_cloud.foundation import PreSharedKey

        return PreSharedKey(_client=self._client, created_at=created_at, endpoint_name=endpoint_name, id=id,)

    def saml2_request(
        self,
        entity_descriptor=None,
        idp_entity_id=None,
        idp_x509_certs=None,
        slo_endpoint=None,
        sp_entity_id=None,
        sso_endpoint=None,
    ):
        """Creates a local `Saml2Request` instance, using the shared SDK context.

        :param entity_descriptor: Contains an entity descriptor document for the identity provider.
            Can be used as an alternative method to provide the identity
            provider's attributes.
        :type entity_descriptor: bytes
        :param idp_entity_id: Entity ID of the identity provider.
        :type idp_entity_id: str
        :param idp_x509_certs: List of public X509 certificates of the identity provider.
            Certificates must be in PEM format.
        :type idp_x509_certs: list
        :param slo_endpoint: URL of the identity provider's SLO endpoint.
        :type slo_endpoint: str
        :param sp_entity_id: Entity ID of the service provider. We recommend that you leave it
            empty and let the system generate it.
        :type sp_entity_id: str
        :param sso_endpoint: URL of the identity provider's SSO endpoint.
        :type sso_endpoint: str
        
        :return: A new instance of a Saml2Request Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.saml2_request.Saml2Request
        """
        from mbed_cloud.foundation import Saml2Request

        return Saml2Request(
            _client=self._client,
            entity_descriptor=entity_descriptor,
            idp_entity_id=idp_entity_id,
            idp_x509_certs=idp_x509_certs,
            slo_endpoint=slo_endpoint,
            sp_entity_id=sp_entity_id,
            sso_endpoint=sso_endpoint,
        )

    def server_credentials(
        self, created_at=None, id=None, server_certificate=None, server_uri=None,
    ):
        """Creates a local `ServerCredentials` instance, using the shared SDK context.

        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param id: Unique entity ID.
        :type id: str
        :param server_certificate: PEM-format X.509 server certificate used to validate the server
            certificate received during the TLS/DTLS handshake.
        :type server_certificate: str
        :param server_uri: Server URI that the client connects to.
        :type server_uri: str
        
        :return: A new instance of a ServerCredentials Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.security.server_credentials.ServerCredentials
        """
        from mbed_cloud.foundation import ServerCredentials

        return ServerCredentials(
            _client=self._client,
            created_at=created_at,
            id=id,
            server_certificate=server_certificate,
            server_uri=server_uri,
        )

    def subtenant_api_key(
        self,
        account_id=None,
        created_at=None,
        creation_time=None,
        groups=None,
        id=None,
        key=None,
        last_login_time=None,
        name=None,
        owner=None,
        status=None,
        updated_at=None,
    ):
        """Creates a local `SubtenantApiKey` instance, using the shared SDK context.

        :param account_id: The ID of the account.
        :type account_id: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param creation_time: The timestamp of the API key creation in the storage, in
            milliseconds.
        :type creation_time: int
        :param groups: A list of group IDs this API key belongs to.
        :type groups: list
        :param id: The ID of the API key.
        :type id: str
        :param key: The API key.
        :type key: str
        :param last_login_time: The timestamp of the latest API key usage, in milliseconds.
        :type last_login_time: int
        :param name: The display name for the API key.
        :type name: str
        :param owner: The owner of this API key, who is the creator by default.
        :type owner: str
        :param status: The status of the API key.
        :type status: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        
        :return: A new instance of a SubtenantApiKey Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.subtenant_api_key.SubtenantApiKey
        """
        from mbed_cloud.foundation import SubtenantApiKey

        return SubtenantApiKey(
            _client=self._client,
            account_id=account_id,
            created_at=created_at,
            creation_time=creation_time,
            groups=groups,
            id=id,
            key=key,
            last_login_time=last_login_time,
            name=name,
            owner=owner,
            status=status,
            updated_at=updated_at,
        )

    def subtenant_dark_theme_color(
        self, color=None, reference=None, updated_at=None,
    ):
        """Creates a local `SubtenantDarkThemeColor` instance, using the shared SDK context.

        :param color: The color given as name (purple) or as a hex code.
        :type color: str
        :param reference: Color name.
        :type reference: str
        :param updated_at: Last update time in UTC.
        :type updated_at: datetime
        
        :return: A new instance of a SubtenantDarkThemeColor Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.branding.subtenant_dark_theme_color.SubtenantDarkThemeColor
        """
        from mbed_cloud.foundation import SubtenantDarkThemeColor

        return SubtenantDarkThemeColor(_client=self._client, color=color, reference=reference, updated_at=updated_at,)

    def subtenant_dark_theme_image(
        self, reference=None, static_uri=None, updated_at=None,
    ):
        """Creates a local `SubtenantDarkThemeImage` instance, using the shared SDK context.

        :param reference: Name of the image.
        :type reference: str
        :param static_uri: The static link to the image.
        :type static_uri: str
        :param updated_at: Last update time in UTC.
        :type updated_at: datetime
        
        :return: A new instance of a SubtenantDarkThemeImage Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.branding.subtenant_dark_theme_image.SubtenantDarkThemeImage
        """
        from mbed_cloud.foundation import SubtenantDarkThemeImage

        return SubtenantDarkThemeImage(
            _client=self._client, reference=reference, static_uri=static_uri, updated_at=updated_at,
        )

    def subtenant_identity_provider(
        self,
        account_id=None,
        created_at=None,
        description=None,
        id=None,
        is_default=None,
        name=None,
        saml2_attributes=None,
        status=None,
        updated_at=None,
    ):
        """Creates a local `SubtenantIdentityProvider` instance, using the shared SDK context.

        :param account_id: The ID of the account the identity provider belongs to.
        :type account_id: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param description: Description for the identity provider.
        :type description: str
        :param id: Entity ID.
        :type id: str
        :param is_default: Flag indicating whether this is the global default identity
            provider.
        :type is_default: bool
        :param name: Name of the identity provider.
        :type name: str
        :param saml2_attributes: Represents SAML2 specific attributes in responses.
        :type saml2_attributes: dict
        :param status: Status of the identity provider.
        :type status: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        
        :return: A new instance of a SubtenantIdentityProvider Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.subtenant_identity_provider.SubtenantIdentityProvider
        """
        from mbed_cloud.foundation import SubtenantIdentityProvider

        return SubtenantIdentityProvider(
            _client=self._client,
            account_id=account_id,
            created_at=created_at,
            description=description,
            id=id,
            is_default=is_default,
            name=name,
            saml2_attributes=saml2_attributes,
            status=status,
            updated_at=updated_at,
        )

    def subtenant_light_theme_color(
        self, color=None, reference=None, updated_at=None,
    ):
        """Creates a local `SubtenantLightThemeColor` instance, using the shared SDK context.

        :param color: The color given as name (purple) or as a hex code.
        :type color: str
        :param reference: Color name.
        :type reference: str
        :param updated_at: Last update time in UTC.
        :type updated_at: datetime
        
        :return: A new instance of a SubtenantLightThemeColor Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.branding.subtenant_light_theme_color.SubtenantLightThemeColor
        """
        from mbed_cloud.foundation import SubtenantLightThemeColor

        return SubtenantLightThemeColor(_client=self._client, color=color, reference=reference, updated_at=updated_at,)

    def subtenant_light_theme_image(
        self, reference=None, static_uri=None, updated_at=None,
    ):
        """Creates a local `SubtenantLightThemeImage` instance, using the shared SDK context.

        :param reference: Name of the image.
        :type reference: str
        :param static_uri: The static link to the image.
        :type static_uri: str
        :param updated_at: Last update time in UTC.
        :type updated_at: datetime
        
        :return: A new instance of a SubtenantLightThemeImage Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.branding.subtenant_light_theme_image.SubtenantLightThemeImage
        """
        from mbed_cloud.foundation import SubtenantLightThemeImage

        return SubtenantLightThemeImage(
            _client=self._client, reference=reference, static_uri=static_uri, updated_at=updated_at,
        )

    def subtenant_policy_group(
        self, account_id=None, apikey_count=None, created_at=None, id=None, name=None, updated_at=None, user_count=None,
    ):
        """Creates a local `SubtenantPolicyGroup` instance, using the shared SDK context.

        :param account_id: The ID of the account this group belongs to.
        :type account_id: str
        :param apikey_count: The number of API keys in this group.
        :type apikey_count: int
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param id: The ID of the group.
        :type id: str
        :param name: The name of the group.
        :type name: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param user_count: The number of users in this group.
        :type user_count: int
        
        :return: A new instance of a SubtenantPolicyGroup Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.subtenant_policy_group.SubtenantPolicyGroup
        """
        from mbed_cloud.foundation import SubtenantPolicyGroup

        return SubtenantPolicyGroup(
            _client=self._client,
            account_id=account_id,
            apikey_count=apikey_count,
            created_at=created_at,
            id=id,
            name=name,
            updated_at=updated_at,
            user_count=user_count,
        )

    def subtenant_trusted_certificate(
        self,
        account_id=None,
        certificate=None,
        certificate_fingerprint=None,
        created_at=None,
        description=None,
        device_execution_mode=None,
        enrollment_mode=None,
        id=None,
        is_developer_certificate=None,
        issuer=None,
        name=None,
        owner_id=None,
        service=None,
        status=None,
        subject=None,
        updated_at=None,
        valid=None,
        validity=None,
    ):
        """Creates a local `SubtenantTrustedCertificate` instance, using the shared SDK context.

        :param account_id: The ID of the account.
        :type account_id: str
        :param certificate: X509.v3 trusted certificate in PEM format.
        :type certificate: str
        :param certificate_fingerprint: A SHA-256 fingerprint of the certificate.
        :type certificate_fingerprint: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param description: Human readable description of this certificate.
        :type description: str
        :param device_execution_mode: Device execution mode where 1 means a developer certificate.
        :type device_execution_mode: int
        :param enrollment_mode: If true, signature is not required. Default value false.
        :type enrollment_mode: bool
        :param id: Entity ID.
        :type id: str
        :param is_developer_certificate: Whether or not this certificate is a developer certificate.
        :type is_developer_certificate: bool
        :param issuer: Issuer of the certificate.
        :type issuer: str
        :param name: Certificate name.
        :type name: str
        :param owner_id: The ID of the owner.
        :type owner_id: str
        :param service: Service name where the certificate is used.
        :type service: str
        :param status: Status of the certificate.
        :type status: str
        :param subject: Subject of the certificate.
        :type subject: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param valid: This read-only flag indicates whether the certificate is valid or
            not.
        :type valid: bool
        :param validity: Expiration time in UTC formatted as RFC3339.
        :type validity: datetime
        
        :return: A new instance of a SubtenantTrustedCertificate Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.security.subtenant_trusted_certificate.SubtenantTrustedCertificate
        """
        from mbed_cloud.foundation import SubtenantTrustedCertificate

        return SubtenantTrustedCertificate(
            _client=self._client,
            account_id=account_id,
            certificate=certificate,
            certificate_fingerprint=certificate_fingerprint,
            created_at=created_at,
            description=description,
            device_execution_mode=device_execution_mode,
            enrollment_mode=enrollment_mode,
            id=id,
            is_developer_certificate=is_developer_certificate,
            issuer=issuer,
            name=name,
            owner_id=owner_id,
            service=service,
            status=status,
            subject=subject,
            updated_at=updated_at,
            valid=valid,
            validity=validity,
        )

    def subtenant_user(
        self,
        account_id=None,
        active_sessions=None,
        address=None,
        created_at=None,
        creation_time=None,
        custom_fields=None,
        email=None,
        email_verified=None,
        full_name=None,
        groups=None,
        id=None,
        is_gtc_accepted=None,
        is_marketing_accepted=None,
        is_totp_enabled=None,
        last_login_time=None,
        login_history=None,
        login_profiles=None,
        password=None,
        password_changed_time=None,
        phone_number=None,
        status=None,
        totp_scratch_codes=None,
        updated_at=None,
        username=None,
    ):
        """Creates a local `SubtenantUser` instance, using the shared SDK context.

        :param account_id: The ID of the account.
        :type account_id: str
        :param active_sessions: List of active user sessions.
        :type active_sessions: list
        :param address: Address.
        :type address: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param creation_time: A timestamp of the user creation in the storage, in milliseconds.
        :type creation_time: int
        :param custom_fields: User's account-specific custom properties. The value is a string.
        :type custom_fields: dict
        :param email: The email address.
        :type email: str
        :param email_verified: A flag indicating whether the user's email address has been
            verified or not.
        :type email_verified: bool
        :param full_name: The full name of the user.
        :type full_name: str
        :param groups: A list of IDs of the groups this user belongs to.
        :type groups: list
        :param id: The ID of the user.
        :type id: str
        :param is_gtc_accepted: A flag indicating that the user has accepted General Terms and
            Conditions.
        :type is_gtc_accepted: bool
        :param is_marketing_accepted: A flag indicating that the user has consented to receive marketing
            information.
        :type is_marketing_accepted: bool
        :param is_totp_enabled: A flag indicating whether two-factor authentication (TOTP) has
            been enabled.
        :type is_totp_enabled: bool
        :param last_login_time: A timestamp of the latest login of the user, in milliseconds.
        :type last_login_time: int
        :param login_history: Timestamps, succeedings, IP addresses and user agent information
            of the last five logins of the user, with timestamps in RFC3339
            format.
        :type login_history: list
        :param login_profiles: A list of login profiles for the user. Specified as the identity
            providers the user is associated with.
        :type login_profiles: list
        :param password: The password when creating a new user. It will be generated when
            not present in the request.
        :type password: str
        :param password_changed_time: A timestamp of the latest change of the user password, in
            milliseconds.
        :type password_changed_time: int
        :param phone_number: Phone number.
        :type phone_number: str
        :param status: The status of the user. ENROLLING state indicates that the user is
            in the middle of the enrollment process. INVITED means that the
            user has not accepted the invitation request. RESET means that the
            password must be changed immediately. INACTIVE users are locked
            out and not permitted to use the system.
        :type status: str
        :param totp_scratch_codes: A list of scratch codes for the two-factor authentication. Visible
            only when 2FA is requested to be enabled or the codes regenerated.
        :type totp_scratch_codes: list
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param username: A username.
        :type username: str
        
        :return: A new instance of a SubtenantUser Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.subtenant_user.SubtenantUser
        """
        from mbed_cloud.foundation import SubtenantUser

        return SubtenantUser(
            _client=self._client,
            account_id=account_id,
            active_sessions=active_sessions,
            address=address,
            created_at=created_at,
            creation_time=creation_time,
            custom_fields=custom_fields,
            email=email,
            email_verified=email_verified,
            full_name=full_name,
            groups=groups,
            id=id,
            is_gtc_accepted=is_gtc_accepted,
            is_marketing_accepted=is_marketing_accepted,
            is_totp_enabled=is_totp_enabled,
            last_login_time=last_login_time,
            login_history=login_history,
            login_profiles=login_profiles,
            password=password,
            password_changed_time=password_changed_time,
            phone_number=phone_number,
            status=status,
            totp_scratch_codes=totp_scratch_codes,
            updated_at=updated_at,
            username=username,
        )

    def subtenant_user_invitation(
        self,
        account_id=None,
        created_at=None,
        email=None,
        expiration=None,
        groups=None,
        id=None,
        login_profiles=None,
        updated_at=None,
        user_id=None,
    ):
        """Creates a local `SubtenantUserInvitation` instance, using the shared SDK context.

        :param account_id: The ID of the account the user is invited to.
        :type account_id: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param email: Email address of the invited user.
        :type email: str
        :param expiration: Invitation expiration as UTC time RFC3339.
        :type expiration: datetime
        :param groups: A list of IDs of the groups the user is invited to.
        :type groups: list
        :param id: The ID of the invitation.
        :type id: str
        :param login_profiles: A list of login profiles for the user. Specified as the identity
            providers the user is associated with.
        :type login_profiles: list
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param user_id: The ID of the invited user.
        :type user_id: str
        
        :return: A new instance of a SubtenantUserInvitation Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.subtenant_user_invitation.SubtenantUserInvitation
        """
        from mbed_cloud.foundation import SubtenantUserInvitation

        return SubtenantUserInvitation(
            _client=self._client,
            account_id=account_id,
            created_at=created_at,
            email=email,
            expiration=expiration,
            groups=groups,
            id=id,
            login_profiles=login_profiles,
            updated_at=updated_at,
            user_id=user_id,
        )

    def trusted_certificate(
        self,
        account_id=None,
        certificate=None,
        certificate_fingerprint=None,
        created_at=None,
        description=None,
        device_execution_mode=None,
        enrollment_mode=None,
        id=None,
        is_developer_certificate=None,
        issuer=None,
        name=None,
        owner_id=None,
        service=None,
        status=None,
        subject=None,
        updated_at=None,
        valid=None,
        validity=None,
    ):
        """Creates a local `TrustedCertificate` instance, using the shared SDK context.

        :param account_id: The ID of the account.
        :type account_id: str
        :param certificate: X509.v3 trusted certificate in PEM format.
        :type certificate: str
        :param certificate_fingerprint: A SHA-256 fingerprint of the certificate.
        :type certificate_fingerprint: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param description: Human readable description of this certificate.
        :type description: str
        :param device_execution_mode: Device execution mode where 1 means a developer certificate.
        :type device_execution_mode: int
        :param enrollment_mode: If true, signature is not required. Default value false.
        :type enrollment_mode: bool
        :param id: Entity ID.
        :type id: str
        :param is_developer_certificate: Whether or not this certificate is a developer certificate.
        :type is_developer_certificate: bool
        :param issuer: Issuer of the certificate.
        :type issuer: str
        :param name: Certificate name.
        :type name: str
        :param owner_id: The ID of the owner.
        :type owner_id: str
        :param service: Service name where the certificate is used.
        :type service: str
        :param status: Status of the certificate.
        :type status: str
        :param subject: Subject of the certificate.
        :type subject: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param valid: This read-only flag indicates whether the certificate is valid or
            not.
        :type valid: bool
        :param validity: Expiration time in UTC formatted as RFC3339.
        :type validity: datetime
        
        :return: A new instance of a TrustedCertificate Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.security.trusted_certificate.TrustedCertificate
        """
        from mbed_cloud.foundation import TrustedCertificate

        return TrustedCertificate(
            _client=self._client,
            account_id=account_id,
            certificate=certificate,
            certificate_fingerprint=certificate_fingerprint,
            created_at=created_at,
            description=description,
            device_execution_mode=device_execution_mode,
            enrollment_mode=enrollment_mode,
            id=id,
            is_developer_certificate=is_developer_certificate,
            issuer=issuer,
            name=name,
            owner_id=owner_id,
            service=service,
            status=status,
            subject=subject,
            updated_at=updated_at,
            valid=valid,
            validity=validity,
        )

    def update_campaign(
        self,
        active_at=None,
        approval_required=None,
        archived_at=None,
        autostop=None,
        autostop_reason=None,
        autostop_success_percent=None,
        campaign_strategy=None,
        created_at=None,
        description=None,
        device_filter=None,
        device_filter_helper=None,
        finished=None,
        id=None,
        name=None,
        phase=None,
        root_manifest_id=None,
        root_manifest_url=None,
        started_at=None,
        starting_at=None,
        stopped_at=None,
        stopping_at=None,
        updated_at=None,
        when=None,
    ):
        """Creates a local `UpdateCampaign` instance, using the shared SDK context.

        :param active_at: The time the campaign entered the active state.
        :type active_at: datetime
        :param approval_required: Flag indicating whether approval is needed to start the campaign.
        :type approval_required: bool
        :param archived_at: The time the campaign was archived.
        :type archived_at: datetime
        :param autostop: Flag indicating whether the campaign should be auto-stopped on
            reaching a threshold.
        :type autostop: bool
        :param autostop_reason: Text description of why a campaign failed to start or why a
            campaign stopped.
        :type autostop_reason: str
        :param autostop_success_percent: Percent of successful device updates to auto stop the campaign.
        :type autostop_success_percent: float
        :param campaign_strategy: How the campaign adds devices. A `one-shot` campaign does not add
            new devices after it has started. A `continuous` campaign means
            that devices may be added to the campaign after it has started.
            The default is `one-shot`.
        :type campaign_strategy: str
        :param created_at: The time the entity was created.
        :type created_at: datetime
        :param description: An optional description of the campaign.
        :type description: str
        :param device_filter: The filter for the devices the campaign targets. Refer to this
            using the filter ID.
        :type device_filter: str
        :param device_filter_helper: Helper for creating the device filter string.
        :type device_filter_helper: mbed_cloud.client.api_filter.ApiFilter
        :param finished: The time the campaign finished.
        :type finished: datetime
        :param id: The campaign ID.
        :type id: str
        :param name: The campaign name.
        :type name: str
        :param phase: The phase of the campaign.
        :type phase: str
        :param root_manifest_id: The ID of the manifest that will be sent to the device as part of
            the campaign.
        :type root_manifest_id: str
        :param root_manifest_url: The URL for the manifest that will be sent to the device as part
            of the campaign.
        :type root_manifest_url: str
        :param started_at: The time the campaign was started.
        :type started_at: datetime
        :param starting_at: The time the campaign will be started.
        :type starting_at: datetime
        :param stopped_at: The time the campaign was stopped.
        :type stopped_at: datetime
        :param stopping_at: The time the campaign will be stopped.
        :type stopping_at: datetime
        :param updated_at: The time the entity was updated.
        :type updated_at: datetime
        :param when: The scheduled start time for the campaign. The campaign will start
            within 1 minute when then start time has elapsed.
        :type when: datetime
        
        :return: A new instance of a UpdateCampaign Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.device_update.update_campaign.UpdateCampaign
        """
        from mbed_cloud.foundation import UpdateCampaign

        return UpdateCampaign(
            _client=self._client,
            active_at=active_at,
            approval_required=approval_required,
            archived_at=archived_at,
            autostop=autostop,
            autostop_reason=autostop_reason,
            autostop_success_percent=autostop_success_percent,
            campaign_strategy=campaign_strategy,
            created_at=created_at,
            description=description,
            device_filter=device_filter,
            device_filter_helper=device_filter_helper,
            finished=finished,
            id=id,
            name=name,
            phase=phase,
            root_manifest_id=root_manifest_id,
            root_manifest_url=root_manifest_url,
            started_at=started_at,
            starting_at=starting_at,
            stopped_at=stopped_at,
            stopping_at=stopping_at,
            updated_at=updated_at,
            when=when,
        )

    def user(
        self,
        account_id=None,
        active_sessions=None,
        address=None,
        created_at=None,
        creation_time=None,
        custom_fields=None,
        email=None,
        email_verified=None,
        full_name=None,
        groups=None,
        id=None,
        is_gtc_accepted=None,
        is_marketing_accepted=None,
        is_totp_enabled=None,
        last_login_time=None,
        login_history=None,
        login_profiles=None,
        password=None,
        password_changed_time=None,
        phone_number=None,
        status=None,
        totp_scratch_codes=None,
        updated_at=None,
        username=None,
    ):
        """Creates a local `User` instance, using the shared SDK context.

        :param account_id: The ID of the account.
        :type account_id: str
        :param active_sessions: List of active user sessions.
        :type active_sessions: list
        :param address: Address.
        :type address: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param creation_time: A timestamp of the user creation in the storage, in milliseconds.
        :type creation_time: int
        :param custom_fields: User's account-specific custom properties. The value is a string.
        :type custom_fields: dict
        :param email: The email address.
        :type email: str
        :param email_verified: A flag indicating whether the user's email address has been
            verified or not.
        :type email_verified: bool
        :param full_name: The full name of the user.
        :type full_name: str
        :param groups: A list of IDs of the groups this user belongs to.
        :type groups: list
        :param id: The ID of the user.
        :type id: str
        :param is_gtc_accepted: A flag indicating that the user has accepted General Terms and
            Conditions.
        :type is_gtc_accepted: bool
        :param is_marketing_accepted: A flag indicating that the user has consented to receive marketing
            information.
        :type is_marketing_accepted: bool
        :param is_totp_enabled: A flag indicating whether two-factor authentication (TOTP) has
            been enabled.
        :type is_totp_enabled: bool
        :param last_login_time: A timestamp of the latest login of the user, in milliseconds.
        :type last_login_time: int
        :param login_history: Timestamps, succeedings, IP addresses and user agent information
            of the last five logins of the user, with timestamps in RFC3339
            format.
        :type login_history: list
        :param login_profiles: A list of login profiles for the user. Specified as the identity
            providers the user is associated with.
        :type login_profiles: list
        :param password: The password when creating a new user. It will be generated when
            not present in the request.
        :type password: str
        :param password_changed_time: A timestamp of the latest change of the user password, in
            milliseconds.
        :type password_changed_time: int
        :param phone_number: Phone number.
        :type phone_number: str
        :param status: The status of the user. ENROLLING state indicates that the user is
            in the middle of the enrollment process. INVITED means that the
            user has not accepted the invitation request. RESET means that the
            password must be changed immediately. INACTIVE users are locked
            out and not permitted to use the system.
        :type status: str
        :param totp_scratch_codes: A list of scratch codes for the two-factor authentication. Visible
            only when 2FA is requested to be enabled or the codes regenerated.
        :type totp_scratch_codes: list
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param username: A username.
        :type username: str
        
        :return: A new instance of a User Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.user.User
        """
        from mbed_cloud.foundation import User

        return User(
            _client=self._client,
            account_id=account_id,
            active_sessions=active_sessions,
            address=address,
            created_at=created_at,
            creation_time=creation_time,
            custom_fields=custom_fields,
            email=email,
            email_verified=email_verified,
            full_name=full_name,
            groups=groups,
            id=id,
            is_gtc_accepted=is_gtc_accepted,
            is_marketing_accepted=is_marketing_accepted,
            is_totp_enabled=is_totp_enabled,
            last_login_time=last_login_time,
            login_history=login_history,
            login_profiles=login_profiles,
            password=password,
            password_changed_time=password_changed_time,
            phone_number=phone_number,
            status=status,
            totp_scratch_codes=totp_scratch_codes,
            updated_at=updated_at,
            username=username,
        )

    def user_invitation(
        self,
        account_id=None,
        created_at=None,
        email=None,
        expiration=None,
        groups=None,
        id=None,
        login_profiles=None,
        updated_at=None,
        user_id=None,
    ):
        """Creates a local `UserInvitation` instance, using the shared SDK context.

        :param account_id: The ID of the account the user is invited to.
        :type account_id: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param email: Email address of the invited user.
        :type email: str
        :param expiration: Invitation expiration as UTC time RFC3339.
        :type expiration: datetime
        :param groups: A list of IDs of the groups the user is invited to.
        :type groups: list
        :param id: The ID of the invitation.
        :type id: str
        :param login_profiles: A list of login profiles for the user. Specified as the identity
            providers the user is associated with.
        :type login_profiles: list
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param user_id: The ID of the invited user.
        :type user_id: str
        
        :return: A new instance of a UserInvitation Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.accounts.user_invitation.UserInvitation
        """
        from mbed_cloud.foundation import UserInvitation

        return UserInvitation(
            _client=self._client,
            account_id=account_id,
            created_at=created_at,
            email=email,
            expiration=expiration,
            groups=groups,
            id=id,
            login_profiles=login_profiles,
            updated_at=updated_at,
            user_id=user_id,
        )

    def verification_response(
        self, message=None, successful=None,
    ):
        """Creates a local `VerificationResponse` instance, using the shared SDK context.

        :param message: Provides details in case of failure.
        :type message: str
        :param successful: Indicates whether the certificate issuer was verified
            successfully.
        :type successful: bool
        
        :return: A new instance of a VerificationResponse Foundation Entity.
        :rtype: mbed_cloud.foundation.entities.security.verification_response.VerificationResponse
        """
        from mbed_cloud.foundation import VerificationResponse

        return VerificationResponse(_client=self._client, message=message, successful=successful,)
