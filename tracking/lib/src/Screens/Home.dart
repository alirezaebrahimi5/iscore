
import 'package:convex_bottom_bar/convex_bottom_bar.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import 'package:tracking/src/Pages/EnterPage.dart';
import 'package:tracking/src/Pages/ItemsPage.dart';
import 'package:tracking/src/Pages/MapPage.dart';
import 'package:tracking/src/Pages/MoneyPage.dart';
import 'package:tracking/src/Pages/TasksPage.dart';
import 'package:tracking/src/Provider/CartProvider.dart';
import 'package:tracking/src/Screens/Cart.dart';
import 'package:badges/badges.dart' as badges;

class Home extends StatefulWidget {
  Home({Key? key}) : super(key: key);

  @override
  Controller createState() =>
    Controller();
}

class Controller extends State {

  int _pageIndex = 0; 
  List<StatelessWidget> pages = [
    TasksPage(),
    MapPage(),
    EnterPage(),
    MoneyPage(),
    ItemsPage()
  ];
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("My sort", style: TextStyle(color: Colors.white),),
        actions: <Widget>[
          badges.Badge(
            badgeContent: Consumer<CartProvider>(
              builder: (context, value, child) {
                return Text(
                  value.getCounter().toString(),
                  style: const TextStyle(
                      color: Colors.white, fontWeight: FontWeight.bold),
                );
              },
            ),
            position: badges.BadgePosition.topStart(),
            child: IconButton(
              onPressed: () {
                Navigator.push(
                    context,
                    MaterialPageRoute(
                        builder: (context) => const CartScreen()));
              },
              icon: const Icon(Icons.shopping_bag_outlined),
            ),
          ),
          const SizedBox(
            width: 20.0,
          ),
          IconButton(
            icon: const Icon(Icons.notifications),
            onPressed: () {
              Navigator.pushNamed(context, '/notifications');
            },
          ), //IconButton
        ], //<Widget>[]
        backgroundColor: Colors.green,
        elevation: 50.0,
        systemOverlayStyle: SystemUiOverlayStyle.light,
      ),
      drawer: Drawer(
        child: Column(
        children: [
          const DrawerHeader(
          decoration: BoxDecoration(
            color: Colors.green,
          ), //BoxDecoration
          child: UserAccountsDrawerHeader(
            decoration: BoxDecoration(color: Colors.green),
            accountName: Text(
            "علیرضا ابراهیمی",
            style: TextStyle(fontSize: 18),
            ),
            accountEmail: Text("۰۹۱۱۸۶۹۱۷۷۹"),
            currentAccountPictureSize: Size.square(50),
            currentAccountPicture: CircleAvatar(
            backgroundColor: Colors.lightGreen,
            child: Text(
              "A",
              style: TextStyle(fontSize: 30.0, color: Colors.white),
            ), //Text
            ), //circleAvatar
          ), //UserAccountDrawerHeader
          ), //DrawerHeader
          ListTile(
          leading: const Icon(Icons.person),
          title: const Text('پروفایل'),
          onTap: () {
            Navigator.pushNamed(context, '/profile');
          },
          ),
          ListTile(
          leading: const Icon(Icons.book),
          title: const Text('تاریخچه'),
          onTap: () {
            Navigator.pushNamed(context, '/history');
          },
          ),
          ListTile(
          leading: const Icon(Icons.workspace_premium),
          title: const Text('امتیازات '),
          onTap: () {
            Navigator.pushNamed(context, '/club');
          },
          ),
          ListTile(
          leading: const Icon(Icons.video_label),
          title: const Text('نمونه ویزیت'),
          onTap: () {
            Navigator.pushNamed(context, '/samples');
          },
          ),
          ListTile(
          leading: const Icon(Icons.headset_mic),
          title: const Text('پشتیبانی'),
          onTap: () {
            Navigator.pushNamed(context, '/ticketing');
          },
          ),
          Expanded(
            child: Align(
              alignment: FractionalOffset.bottomCenter,
              child: 
                ListTile(
                  leading: const Icon(Icons.logout),
                  title: const Text('خروج'),
                  onTap: () {
                    Navigator.pop(context);
                  },
                ),
            )
          )
        ],
        ),
      ), //Drawer
      body: pages[_pageIndex],
      bottomNavigationBar: ConvexAppBar(
        height: 60, 
        backgroundColor: Colors.green,

        items: const[ 
            TabItem(icon: Icons.checklist_rtl, title: 'وظایف'),
            TabItem(icon: Icons.map, title: 'مسیر من'),
            TabItem(icon: Icons.add, title: 'ثبت'),
            TabItem(icon: Icons.monetization_on_outlined, title: 'کارکرد'),
            TabItem(icon: Icons.shopping_cart_outlined, title: 'محصولات'),
          ], 
        onTap: (int i) {
          setState(() { 
            _pageIndex = i; 
          }); 
        },
      )
    );
  }
}