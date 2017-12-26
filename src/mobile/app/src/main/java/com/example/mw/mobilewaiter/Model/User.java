package com.example.mw.mobilewaiter.Model;

/**
 * Created by andre on 24.11.2017.
 */

public class User {
    private String Name;
    private String Password;
    private String Phone;
    private String Table;

    public User() {

    }
    public User(String name, String password) {
        Name = name;
        Password = password;
    }

    public String getPhone() {
        return Phone;
    }

    public void setPhone(String phone) {
        Phone = phone;
    }

    public String getName() {
        return Name;
    }

    public void setName(String name) {
        Name = name;
    }

    public String getPassword() {
        return Password;
    }

    public void setPassword(String password) {
        Password = password;
    }

    public String getTable() { return Table; }

    public void setTable(String table) { Table = table; }
}
