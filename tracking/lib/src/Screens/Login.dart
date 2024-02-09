import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:tracking/src/Screens/Home.dart';
import 'package:tracking/src/Service/Api.dart';

class SignIn extends StatefulWidget {
  const SignIn({Key? key}) : super(key: key);

  static const route = '/login';

  @override
  State<SignIn> createState() => _SignInState();
}

class _SignInState extends State<SignIn> {
  TextEditingController mobileController = TextEditingController();
  TextEditingController passwordController = TextEditingController();

  login() async {
    var data = {
      'mobile': mobileController.text,
      'password': passwordController.text,
    };

    var res = await Api().login(data);
    var body = json.decode(res.body);

    if (body['code'] == 401) {
      ScaffoldMessenger.of(context)
          .showSnackBar(const SnackBar(content: Text('نام کاربری یا رمز عبور اشتباه است')));
    }

    if (body['access'] != null) {
      SharedPreferences localStorage = await SharedPreferences.getInstance();
      localStorage.setString('access', body['access']);
      localStorage.setString('refresh', body['refresh']);

      Navigator.push(
          context, MaterialPageRoute(builder: (context) => Home()));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            TextField(
              controller: mobileController,
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                hintText: 'شماره همراه',
                labelStyle: TextStyle(fontSize: 18),
              ),
            ),
            const SizedBox(height: 24),
            TextField(
              controller: passwordController,
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                hintText: 'رمز عبور',
                labelStyle: TextStyle(fontSize: 18),
              ),
            ),
            const SizedBox(height: 24),
            Align(
              alignment: Alignment.center,
              child: ElevatedButton(
                onPressed: () {
                  login();
                },
                child: const Text(
                  'ورود',
                  style: TextStyle(fontSize: 16),
                ),
              ),
            ),
            const SizedBox(height: 16),
          ],
        ),
      ),
    );
  }
}