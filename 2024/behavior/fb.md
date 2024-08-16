most pround project
---
Multi channel optimization
Late last year, i joined a team to help them build and improve model performance. The model is a regression model to predict order volume for a store if it runs a certain promotion. That was all going well. We launched the model and the product. But when i later tried improve the model, the offline evaluations all show promising results but when it went into production, it wasnt showing the corresponding positive business metrics. I dug into downstream services and understood how the model results was being used and found out the reason. This product is eseentially helping restaurants to optimize their promotion strategies on the delivery platforms which is helping them to spend the money more wisely. Since it is related to money spending, the users usually set a budget to restrict how much they want to spend. When the campaign spends more than the budget, we will stop running promotions for them. And i noticed during the experiments, a lot of campaigns are having early pauses issues which is diminishing the model improvement. 

After then, I proposed a new product design to the PM which would allow us to smartly allocate the budget across multiple stores and multiple days and avoid early pauses. To persuade the PM, I implemented a simple simulation to estimate the headroom and presented the results. After he got onboarded, I drafted the RFC to document the new architecture of the backend service. Since this architecutre change involves multiple teams' service, I had rounds of RFC review meetings to walk throught the designs and address their questions and concerns. The biggest concern or conflict comes from a team because my proposed changes totally refactored their service and the new architecture seems quite complex to them, and they were worries that the potential maintanence cost and oncall load. After talking to their tech lead and the team, I understood their concerns and volunteered to do several knowledgre share meetings to walk through the team on the new change to make sure they understand the problem and solution well. 

This new product change is a joined effort across multiple teams. I mainly oversees the overall progress and drives the weekly meeting to track the timeline. Meanwhile I talked the OPs and Sales team to make sure they are aware of this new paradiagm and understand what this means and wrote a tech blog and runbook to help them explain the product and answer questions from the users. Finally we successully launched this new product in time and siginificantly improved the business metrics. The experiment we ran was showing 7% order volume increase which is a huge win for both the customers and us.



xfunc conflict
---
This is a project I led last year in Future Foods team. The business model of this product is to find restaurants as our fulfillment stores and open online stores on doordash and ubereats. We have the control of the prices and promotions and pay a fixed amount of money to the restaurants.

The project is trying to update the store prices so it becomes more competitive. We built a hexagon based menu item pricing index and updated the prices to median of the market. Most stores are reducing prices. And this mechanisim becomes the way to set prices for new stores. And we have done experiments to verify updating the prices bring our  

However during the launch, we got a lot of push backs from Operations and Sales due to different reasons. After meeting with them and clarify on what they wants and are concerned, I realized this is acutally a quite hard conflict and might jeopordize the launch.To help you understand this issue, let me first explain how this product works: if we look at an order's value, half of them will go to the restaurants, 20% goes to the ofo, 30% will become ours(Ops will use part of it to run promotions). If we reduce the prices, it will become hard for sales to find restaurants and ops to run promotions to hit their monthly revenue target.

After understanding their concerns, I had serveral rounds of meetings to explain what experiments we have ran and what it means to make sure they understand reducing price is good for everyone and prepare docs and runbook to help sales to explain how we get this nnumber. And meanwhile we propose several processes to further alleviate their concerns. 
For sales, we build an exception process so that if sales get strong push back from restaurants, sales can input their expected number and use our tool to check how competitive it is. If it is not higher than 50% we will approve this request automatically.


xfunc conflict
---
This is also related to the boost product. After we launched the product successfully, I know this is actually also a good fit for another product in our company. This product is helping restaurants to open virtual brands on the delivery platforms and rely on the restaurant owners to fullfil the orders. They will be responsible for managing these stores. They have a dedicated OPs team to schedule promotions for these stores manually. I briefly walked through them about this product. They were quite interested but also hesitant to use. They claimed that they have better undertandings on each stores and they want flexibilities to run different promotions to achieve various goals based on the business needs since our product only optimize revenue. Although we have ran experiments to show that our product can help generate more revenue than theirs, we do not have the flexiblities to fulfill different needs. So we started a work thread to implement these new features to support maximizing different objectives and also started another working thread to build a tool for them to start to use. I persuaded them to start using the tool to run promotions instead of going to the delivery platform to do so. And in the tool, they can see what the model suggests and the corresponding predictions. The goal is to let them get used to the results and build trust with it. If they dont like the model's suggestion, they can still go with their instincts. 



Tell me about a time that a peer or manager gave you specific, actionable feedback for improvement.


Tell me about a time you had to pivot mid-project due to project requirements or stakeholder expectations changing.


Tell me about the most difficult working relationship that you've had.


Tell me about a time when you faced pushback regarding your approach on a project.

Tell me about a time when you had to adopt an experimental approach to resolving something.


Tell me about a time a leader asked you to do something that you didn't view as the highest priority


Tell me about a time when you volunteered to take on an important portion of a critical project.



Tell me about a time when you needed to act quickly on something but did  not have a clear idea on how to best proceed.


Tell me about a time when you didn't have all of the desired information to solve a technical problem and how it was resolve.


Describe a time when you had to quickly learn something new and complex in order to ramp up for a project or solve a problem.



Tell me about a time when you needed to overcome a barrier in your work to achieve an end result.




Tell me about a time when you had to manage competing priorities in order to deliver on a project.



Tell me about a time when you faced a significant setback that forced you to reprioritize your work.



Tell me about a result you achieved for your team that you are most proud of.



Tell me about a project you were on that grew in scope and timeline in an unexpected way.



Tell me about a time when you took initiative to complete an important project for your team.


What is a current area of improvement or development for you?



Tell me a specific example of how a new skill set you grew in recent years helped you improve.



Describe a decision you disagreed with, and how it impacted your work.


How did you build your knowledge of the technical details in this space?


Tell me about a time when a project you were on failed to meet agreed upon requirements (e.g. deadline, key deliverables, etc.)



Tell me about a time you needed to push for a change that you knew would be unpopular with some people.



Tell me about a time you disagreed with a colleague and later found out your initial stance was not entirely correct.



Tell me about a specific skill set you developed after observing peers or mentors leveraging such skills.




Describe a specific example that demonstrates how you have balanced your own professional development with the day-to-day demands of your role.