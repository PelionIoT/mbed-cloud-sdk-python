Feature: Subscribe to device events

    @StopNotifications
    Scenario: Demonstrate timeout when getting first device event
        Given we have an MbedCloud
        When we subscribe to a registration device event
            And we request the first value
        Then we get a timeout

    @StopNotifications
    Scenario: Recieve a notification for registration event
        Given we have an MbedCloud
        When we subscribe to a registration device event
            And we listen for notifications
        Then we receive a notification