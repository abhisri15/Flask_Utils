from migrate import db, create_app, Member, Order

app = create_app()

def display_table_data(title, data, columns):
    print(f"\n{title}")
    print(" | ".join(columns))
    print("-" * 80)
    for row in data:
        print(" | ".join(str(getattr(row, col)) for col in columns))


with app.app_context():

    # Fetch and print Customer data
    customers = Member.query.all()
    display_table_data("Member", customers, ['id', 'name'])

    # Fetch and print Customer data
    orders = Order.query.all()
    display_table_data("Order", orders, ['id', 'total'])

    # # Order_product table
    # stmt = order_product.select()
    # result = db.session.execute(stmt)

    # print("\norder_product table")
    # print("order_id | product_id")
    # print("-" * 30)
    # for row in result:
    #     print(f"{row.order_id} | {row.product_id}")