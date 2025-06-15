#Author: your.email@your.domain.com
#Keywords Summary :
#Feature: List of scenarios.
#Scenario: Business rule through list of steps with arguments.
#Given: Some precondition step
#When: Some key actions
#Then: To observe outcomes or validation
#And,But: To enumerate more Given,When,Then steps
#Scenario Outline: List of steps for data-driven as an Examples and <placeholder>
#Examples: Container for s table
#Background: List of steps run before each of the scenarios
#""" (Doc Strings)
#| (Data Tables)
#@ (Tags/Labels):To group Scenarios
#<> (placeholder)
#""
## (Comments)
#Sample Feature Definition Template
@OrangeHRMLoginFeature
Feature: Orange HRM Login feature

  @LOG_TC_001
  Scenario: Validate navigation to OrangeHRM Login page
    Given Chrome browser is launched
    When User navigates to OrangeHRM Login page
    Then User should able to see auth/login in current page url

  @LOG_TC_002
  Scenario: Validate login to OrangeHRM site
    Given Chrome browser is launched
    When User navigates to OrangeHRM Login page
    And User enters username
    And User enters password
    And User clicks on login button
    Then User should able to see dashboard/index in current page url

  @LOG_TC_003
  Scenario: OrangeHRM Login with parameters
    Given Chrome browser is launched
    When User navigates to OrangeHRM Login page
    And User enters username "Admin"
    And User enters password "admin123"
    And User clicks on login button
    Then User should able to see "dashboard/index" in current page url
  
  #@tag2
  #Scenario Outline: Title of your scenario outline
    #Given I want to write a step with <name>
    #When I check for the <value> in step
    #Then I verify the <status> in step
#
    #Examples: 
      #| name  | value | status  |
      #| name1 |     5 | success |
      #| name2 |     7 | Fail    |
