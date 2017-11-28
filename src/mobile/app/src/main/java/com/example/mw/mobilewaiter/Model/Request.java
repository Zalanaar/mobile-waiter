package com.example.mw.mobilewaiter.Model;

import java.util.List;

/**
 * Created by Vladislav_Kostusev on 28.11.2017.
 */

public class Request {
    private String phone;
    private String name;
    private  String table;
    private String total;
    private List<Order> foods;

    public Request(){}

    public Request(String phone, String name, String table, String total, List<Order> foods) {
        this.phone = phone;
        this.name = name;
        this.table = table;
        this.total = total;
        this.foods = foods;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getTable() {
        return table;
    }

    public void setTable(String table) {
        this.table = table;
    }

    public String getTotal() {
        return total;
    }

    public void setTotal(String total) {
        this.total = total;
    }

    public List<Order> getFoods() {
        return foods;
    }

    public void setFoods(List<Order> foods) {
        this.foods = foods;
    }
}
