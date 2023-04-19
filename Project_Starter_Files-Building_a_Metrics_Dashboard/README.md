**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

-Default Namespace :

![running k8s pods in default namespace](https://user-images.githubusercontent.com/88302867/231969936-63a94f7f-136a-4c81-b40e-80073f2a191d.PNG)

-Monitoring Namespace :

![running k8s pods in monitoring namespace](https://user-images.githubusercontent.com/88302867/231970097-95e7dd12-c90e-4e7d-93bc-754ee81cbdbd.PNG)

-Observability Namespace :

![running k8s pods in obervability namespace](https://user-images.githubusercontent.com/88302867/232361625-7c6a26c2-f46b-4b83-8ae7-bcf75eb39363.PNG)



## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

![grafana_homepage](https://user-images.githubusercontent.com/88302867/232175181-860c6a79-7011-4c52-9d10-af5e007940f5.PNG)



## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

![grafana_dashboard](https://user-images.githubusercontent.com/88302867/232175687-699dbbae-266e-4d0c-be26-5f7536dd18b0.PNG)


## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

-SLI based on ***monthly uptime*** :
 The avarage uptime service during month of April was 98.65%

-SLI based on ***request response time*** :
 The average time taken to return a request during the month of April was 156 ms.

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 

1. **Service Availabilty** This metric is to help indicate the up time service during certain of time
2. **CPU and Memory Usage** This metric is to address whether hte services have a performance issue and to monitor the utilization so we can prepare for the scaling.
3. **Error Rate** This metric is to measures the number of failures that occur during a given period 
4. **Response Time** This metric is to measure the latency of the services
5. **Throughput** This metric is to monitor and measure the number of load that a services can handle


## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

![Application Dashboard](https://user-images.githubusercontent.com/88302867/232179596-488ba30f-0495-49c5-ac79-f8962f1b2474.PNG)


## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.

Jaeger UI 

![JaegerUI](https://user-images.githubusercontent.com/88302867/232944587-41b66cf8-27b2-4ca0-98cd-1998174c0313.PNG)


Backend app span:

![span backendapp](https://user-images.githubusercontent.com/88302867/232370784-169e69c7-c50a-4275-82b6-52545f2e4081.PNG)


## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

![Jaeger Dashboard](https://user-images.githubusercontent.com/88302867/232376469-d99a90dd-d8e7-42bf-8710-ec05cdeac78a.PNG)


## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

TROUBLE TICKET

Name: Putu A

Date: 19 April 2023 08:59:37

Subject: Error 404 when accessing homepage button

Affected Area: APi call

Severity: High

Description: when hit button (localhost:8080/favicon.ico), page can not be found

![span error](https://user-images.githubusercontent.com/88302867/232948069-29a53a64-7145-4594-8d18-984612ea4758.PNG)



## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

**SLI**
1. Error rate is less than 10 in 24 hours
2. Response time is less than 2000ms per minute
3. 75% more successful responses than errors
4. The average CPU and Memory utilization resource is less than 75% per month

**SLO**
1. 99.9% uptime per month
2. 99.9% of responses to our front-service will return 2xx, 3xx or 4xx HTTP code within 2000 ms
3. 99.99% of transaction requests will succeed in a month
4. The CPU usage and memory usage should be less than 85% for last 30 days

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

**1. Less than 10 error in 24 Hours**

     Error requests per minute indicates error coming in a system. So we can detect the error early
     
**2. Average response time is less than 2000ms in 24 Hours**

     Average response time will show average response time for services, so we can make sure that no any performance issue accessing the app
     
**3. Successful response > 75% more than errors**

     More successful response means our app is in healthy state
     
**4. Monthly Average Resource Utilization (CPU and Memory) is less than 85%**

     To prevent from systems degrade in performance 
     
## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  

![Application Dashboard](https://user-images.githubusercontent.com/88302867/232380187-a12f8163-25c2-46e7-b2b1-c1b712bb2a6c.PNG)

Application stats -> Show available app service

Successful requests -> Show total succesful request per app

Error requests - Shows the total 40x and 50x error requests per service

Average response time - Shows the average response time successful requests per service

Average memory - Shows the average memory used per service

Average CPU used - Shows the average CPU used per service

Network I/O - Shows the amount of I/O operations per minute in the nod


