#sql-training


# sample chinook queries below
-- 2020-03-16 11:44:52.1270
SELECT "rowid" as rowid,* FROM  "albums" ORDER BY 1 LIMIT 300 OFFSET 0;

-- 2020-03-16 11:44:52.1300
SELECT COUNT(*) as count FROM  "albums";

-- 2020-03-16 12:08:45.7820
SELECT *

-- 2020-03-16 12:12:12.4560
SELECT COUNT(*) as count FROM  "albums";

-- 2020-03-16 12:12:23.8590
SELECT COUNT(*) as count FROM  "albums";

-- 2020-03-16 12:12:51.6040
SELECT COUNT(*) as count FROM  "albums";

these were in my sql table reader when I opened it so I figured I would include it here. 



# place holder ryan meckings method 


# David dodds technique ... 
SELECT
count (DISTINCT charactercreator_character.character_id) AS total_characters
,COUNT (DISTINCT charactercreator_mage.character_ptr_id) - COUNT (DISTINCT charactercreator_necromancer.mage_ptr_id)  AS just_mages
,COUNT (DISTINCT charactercreator_necromancer.mage_ptr_id) AS necromancers
,COUNT (DISTINCT charactercreator_thief.character_ptr_id) AS theives
,COUNT (DISTINCT charactercreator_cleric.character_ptr_id) AS clerics
,COUNT (DISTINCT charactercreator_fighter.character_ptr_id) AS fighters
FROM charactercreator_character
,charactercreator_mage
,charactercreator_necromancer
,charactercreator_thief
,charactercreator_cleric
,charactercreator_fighter


# Chris Jacuk 
This is chris jacuks method for trying this out 
# Question 2: How many of each specific subclass?
charachter_types_items = ['charactercreator_mage',
                    'charactercreator_thief',
                    'charactercreator_cleric',
                    'charactercreator_fighter']
subclasses = ['mage','thief','cleric','fighter']
print("How many of each specific subclass?")
i = 0
for items in charachter_types_items:
    subclass_query = f"""
    SELECT
        count(distinct character_ptr_id) as subclass_count
    FROM
        {items}
     """
    subclass_result = cursor.execute(subclass_query).fetchone()
    print(f"There are {subclass_result[0]} charcters of subclass {subclasses[i]}")
    i += 1 

    