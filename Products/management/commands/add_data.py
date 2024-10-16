from Products.models import Category
    
electronics = Category.objects.create(name="Electronics & Appliances")
fashion = Category.objects.create(name="Fashion & Apparel")
beauty = Category.objects.create(name="Beauty & Personal Care")
grocery = Category.objects.create(name="Grocery & Food Items")
home = Category.objects.create(name="Home & Furniture")
sports = Category.objects.create(name="Sports & Outdoor")
books = Category.objects.create(name="Books & Stationery")
toys = Category.objects.create(name="Toys & Baby Products")
health = Category.objects.create(name="Health & Wellness")
automotive = Category.objects.create(name="Automotive")
office = Category.objects.create(name="Office & Business Supplies")
pets = Category.objects.create(name="Pet Supplies")
tools = Category.objects.create(name="Tools & Hardware")
travel = Category.objects.create(name="Travel & Luggage")
entertainment = Category.objects.create(name="Entertainment & Subscriptions")

# Subcategories for Electronics & Appliances
Category.objects.create(name="Mobile Phones & Accessories", parent=electronics)
Category.objects.create(name="Laptops, Desktops & Tablets", parent=electronics)
Category.objects.create(name="Televisions & Home Entertainment", parent=electronics)
Category.objects.create(name="Cameras & Photography Equipment", parent=electronics)
Category.objects.create(name="Smartwatches & Wearables", parent=electronics)
Category.objects.create(name="Home Appliances (Refrigerators, ACs, Washing Machines)", parent=electronics)
Category.objects.create(name="Kitchen Appliances (Microwave Ovens, Coffee Makers)", parent=electronics)
Category.objects.create(name="Gaming Consoles & Accessories", parent=electronics)

# Subcategories for Fashion & Apparel
Category.objects.create(name="Men’s Clothing (Shirts, T-Shirts, Jackets)", parent=fashion)
Category.objects.create(name="Women’s Clothing (Dresses, Kurtis, Sarees)", parent=fashion)
Category.objects.create(name="Kids’ Clothing", parent=fashion)
Category.objects.create(name="Footwear (Shoes, Sandals, Boots)", parent=fashion)
Category.objects.create(name="Bags & Backpacks", parent=fashion)
Category.objects.create(name="Jewelry & Accessories (Watches, Sunglasses, Hats)", parent=fashion)

# Subcategories for Beauty & Personal Care
Category.objects.create(name="Skincare (Moisturizers, Serums)", parent=beauty)
Category.objects.create(name="Haircare (Shampoos, Conditioners)", parent=beauty)
Category.objects.create(name="Makeup (Lipsticks, Foundations)", parent=beauty)
Category.objects.create(name="Fragrances (Perfumes, Deodorants)", parent=beauty)
Category.objects.create(name="Personal Hygiene (Sanitizers, Body Wash)", parent=beauty)
Category.objects.create(name="Grooming Kits & Tools", parent=beauty)

# Subcategories for Grocery & Food Items
Category.objects.create(name="Fresh Fruits & Vegetables", parent=grocery)
Category.objects.create(name="Beverages (Tea, Coffee, Soft Drinks)", parent=grocery)
Category.objects.create(name="Snacks & Packaged Foods", parent=grocery)
Category.objects.create(name="Cooking Essentials (Oil, Spices, Flour)", parent=grocery)
Category.objects.create(name="Dairy Products (Milk, Butter, Cheese)", parent=grocery)
Category.objects.create(name="Organic & Health Foods", parent=grocery)

# Subcategories for Home & Furniture
Category.objects.create(name="Furniture (Beds, Sofas, Tables)", parent=home)
Category.objects.create(name="Home Decor (Wall Art, Curtains)", parent=home)
Category.objects.create(name="Kitchenware & Cookware (Utensils, Pans)", parent=home)
Category.objects.create(name="Bedding & Mattresses", parent=home)
Category.objects.create(name="Cleaning Supplies (Mops, Brooms)", parent=home)
Category.objects.create(name="Lighting (Lamps, Chandeliers)", parent=home)

# Subcategories for Sports & Outdoor
Category.objects.create(name="Gym Equipment (Treadmills, Dumbbells)", parent=sports)
Category.objects.create(name="Sportswear & Shoes", parent=sports)
Category.objects.create(name="Outdoor Gear (Tents, Camping Tools)", parent=sports)
Category.objects.create(name="Bicycles & Accessories", parent=sports)
Category.objects.create(name="Fitness Trackers", parent=sports)

# Subcategories for Books & Stationery
Category.objects.create(name="Academic Books & Textbooks", parent=books)
Category.objects.create(name="Fiction & Non-Fiction Books", parent=books)
Category.objects.create(name="E-Books & Audiobooks", parent=books)
Category.objects.create(name="Office Supplies (Pens, Notebooks)", parent=books)
Category.objects.create(name="Art & Craft Supplies", parent=books)

# Subcategories for Toys & Baby Products
Category.objects.create(name="Toys & Games (Board Games, Action Figures)", parent=toys)
Category.objects.create(name="Baby Clothing & Shoes", parent=toys)
Category.objects.create(name="Diapers & Wipes", parent=toys)
Category.objects.create(name="Feeding Essentials (Bottles, High Chairs)", parent=toys)
Category.objects.create(name="Baby Gear (Strollers, Car Seats)", parent=toys)

# Subcategories for Health & Wellness
Category.objects.create(name="Medicines & Healthcare Products", parent=health)
Category.objects.create(name="Supplements & Vitamins", parent=health)
Category.objects.create(name="Medical Devices (Thermometers, Blood Pressure Monitors)", parent=health)
Category.objects.create(name="First Aid Kits", parent=health)

# Subcategories for Automotive
Category.objects.create(name="Car Accessories (Covers, Floor Mats)", parent=automotive)
Category.objects.create(name="Bike Accessories (Helmets, Gloves)", parent=automotive)
Category.objects.create(name="Tires & Vehicle Parts", parent=automotive)
Category.objects.create(name="Car Electronics (Dashcams, GPS)", parent=automotive)

# Subcategories for Office & Business Supplies
Category.objects.create(name="Office Furniture (Chairs, Desks)", parent=office)
Category.objects.create(name="Printers & Scanners", parent=office)
Category.objects.create(name="Projectors & Presentation Tools", parent=office)
Category.objects.create(name="Office Storage & Organization", parent=office)

# Subcategories for Pet Supplies
Category.objects.create(name="Pet Food & Treats", parent=pets)
Category.objects.create(name="Pet Grooming Products", parent=pets)
Category.objects.create(name="Pet Toys & Accessories", parent=pets)
Category.objects.create(name="Aquariums & Fish Supplies", parent=pets)

# Subcategories for Tools & Hardware
Category.objects.create(name="Power Tools (Drills, Grinders)", parent=tools)
Category.objects.create(name="Hand Tools (Hammers, Screwdrivers)", parent=tools)
Category.objects.create(name="Electrical Supplies (Wires, Switches)", parent=tools)
Category.objects.create(name="Paints & Coatings", parent=tools)

# Subcategories for Travel & Luggage
Category.objects.create(name="Suitcases & Trolleys", parent=travel)
Category.objects.create(name="Travel Accessories (Neck Pillows, Travel Adapters)", parent=travel)
Category.objects.create(name="Backpacks & Duffel Bags", parent=travel)

# Subcategories for Entertainment & Subscriptions
Category.objects.create(name="Music CDs & Vinyl Records", parent=entertainment)
Category.objects.create(name="Movie DVDs & Blu-rays", parent=entertainment)
Category.objects.create(name="Online Subscriptions (Streaming, Software Licenses)", parent=entertainment)
