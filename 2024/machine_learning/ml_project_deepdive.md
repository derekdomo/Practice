# Overview
Multi channel optimization product
- pricing
- promotion
- advertisement
- coupon
Suggest the optimal and personalized strategies of the four channels for each customer

# High level components
- Offline
    - ETL & Model Training
- Online
    - Service layer 
        - Orchestration: cadence
            - campaign based workflow
        - Plan Generation & Scoring
        - Solver
        - Plan Execution  

# Deep dive
- Regression model - lightgbm
    - model objective
        - revenue prediction model
        - promotion spend prediction model
        - ads spend prediction model
    - feature set
        - historical perf feature(l7d, l30d)
        - store meta data feature
            - menu
            - cuisine
            - neighborhood demographics
            - neighborhood similar restaurants
        - promo meta data feature
        - ads meta data feature
        - pricing meta data feature
    - data split
        - split by dates
            - l45 - l15 as training
            - l15 - l5 as validation
    - experimented model
        - DNN
        - Wide and Deep
        - lightgbm

- Solver
    - Campaign optimization within a week constrained by a fixed budget
    - Plan Enumeration:
        - a store with a promotion strategy, pricing strategy and ads strategy tuple
    - Objective MIP: maximizing total revenue over a week
        - constraints:
            - total_predicted_promo_spend + total_predicted_ads_spend < budget
            - only one plan can be selected for a store on a single day
        - continuous solve for the remaining of the week with updated budget

- Plan Execution
    - Delivery platform integration
    - Pricing service
    - Coupon service

- Experimentation
    - Campaign switchback

