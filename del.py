
Am a azure data engineer and i got the below question when in attended as an azure data interview
  
    
I answered like above, Are these points valied for the above question, please validate my points, and let me know if any point mentioned above is not correct for this question, and also give me your possbility others answers / points for this question to make my panne happy. 
  
 



---




18	 How would you optimize the performance of a Spark job with high data shuffling?

Naga:
----
    1) drop duplicates
    2) select necessary columns only
    3) increase spark.sql.shuffle.partition as per scenario
    4) enable AQE
    5) apply saltinig in case we are going for joins
    6) avoid wide tranformations if possible
    7) increase executer memory
    8) kryo serialize
    poton enabled
    off-heap memory
    tongstun serialize

     increase nodes
    
    
Chiru:
------
    1) if using older version enable AQE / spark.sql.shuffle.partion(250)
    2) apply salting methodoloy if there is a data skewness
    2) create a bucketed table and join bucket table with bucketed table
    3) repartition by increasing the parallelism
    3) apply partition by
    4) unpersist the unused dataframe
    5) select necessary columns
    6) filter the data as early possible
    7) enable photon in the cluster
    8) drop duplicates
    9) if posibble avoid un-necessary wide transformation
    10) make use of tungstun serializer
    11) Checkpoint (for streaming data and getting the data from rdbms)
    
        
Abhi:
-----
    - avoid unnecessary joins/ avoid wide transformations
    - apply repartition
    - checkpointing


Pradip:
    avaoid wide transformation if possible
    user repartiton with key
    brodcast
    partitoning
    caching
    use right joining statergy
    enable aqe









***************



18	 How would you optimize the performance of a Spark job with high data shuffling?
34	 How do you process large CSV files without running into memory issues?
40	 Are you aware of CapTheorem?
35	 How would you ensure data consistency and reliability in a distributed system?
54	 What is the difference between S3 buckets and Hive buckets?
55	 What ETL tools have you used? Can you describe your experience with them?
56	 What is BigQuery, and how do you use it? Can you explain the syntax for BigQuery?
55		What is the difference between search() and match()?
47	 What are the tables you have used so far? Can you provide some names of the tables?
48	 Are these tables dimension tables or fact tables?
49	 What is a dimension table, and what is a fact table?
50	 What are the different types of dimensions available?




