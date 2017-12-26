package com.example.mw.mobilewaiter;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.View;
import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.TextView;
import android.widget.Toast;

import com.example.mw.mobilewaiter.Common.Common;
import com.example.mw.mobilewaiter.Interface.ItemClickListener;
import com.example.mw.mobilewaiter.Model.Category;
import com.example.mw.mobilewaiter.Model.Request;
import com.example.mw.mobilewaiter.Model.User;
import com.example.mw.mobilewaiter.ViewHolder.MenuViewHolder;
import com.firebase.ui.database.FirebaseRecyclerAdapter;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.google.zxing.integration.android.IntentIntegrator;
import com.squareup.picasso.Picasso;

import java.util.Timer;

public class Home extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {

    FirebaseDatabase database;
    DatabaseReference category;
    DatabaseReference wait_req;
    TextView txtFullName;
    String restaurantId;
    String string;
    String restaurantTable;
    Integer key = 0;
    DataSnapshot dataSnapshot;

    RecyclerView recycler_menu;
    RecyclerView.LayoutManager layoutManager;

    FirebaseRecyclerAdapter<Category,MenuViewHolder> adapter;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        toolbar.setTitle("Menu");
        setSupportActionBar(toolbar);

        //Init Firebase
        database = FirebaseDatabase.getInstance();
        category = database.getReference("Category");
        wait_req = database.getReference("Waiters Requests");

        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
               Intent cartIntent = new Intent(Home.this,Cart.class);
               startActivity(cartIntent);
            }
        });

        FloatingActionButton wait = (FloatingActionButton) findViewById(R.id.wait_btn);
        wait.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                wait_req.addValueEventListener(new ValueEventListener() {
                    @Override
                    public void onDataChange(DataSnapshot dataSnapshot) {

                        //check user in db
                        if (dataSnapshot.child(Common.currentUser.getPhone()).exists()) {
                            key = 2;
                        } else {
                            key = 1;
                        }
                    }

                    @Override
                    public void onCancelled(DatabaseError databaseError) {

                    }
                });

                if (key == 1){
                    Toast.makeText(Home.this, "Please wait! Your waiter is on the way!", Toast.LENGTH_SHORT).show();
                    Request request = new Request(
                            Common.currentUser.getTable()
                    );
                    wait_req.child(String.valueOf(Common.currentUser.getPhone()))
                            .setValue(request);
                }
                else if (key > 1){
                    Toast.makeText(Home.this, "You have already called the waiter!", Toast.LENGTH_SHORT).show();
                }

            }
        });

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.addDrawerListener(toggle);
        toggle.syncState();

        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);

        // set name for user
        View headerView = navigationView.getHeaderView(0);
        txtFullName = (TextView)headerView.findViewById(R.id.txtFullName);
        txtFullName.setText(Common.currentUser.getName());

        //load menu
        recycler_menu = (RecyclerView)findViewById(R.id.recycler_menu);
        recycler_menu.setHasFixedSize(true);
        layoutManager = new LinearLayoutManager(this);
        recycler_menu.setLayoutManager(layoutManager);

        if(Common.isConnectedToInternet(this))
            loadMenu(restaurantId);
        else
        {
            Toast.makeText(this, "Please check your connection!", Toast.LENGTH_SHORT).show();
            return;
        }





        //get intent here
        if(getIntent() != null)
            string = getIntent().getStringExtra("RestaurantId");
            String[] parts = string.split("-");
            String part1 = parts[0];
            String part2 = parts[1];
            restaurantId = part1;
            restaurantTable = part2;

        if(!restaurantId.isEmpty() && restaurantId != null)
        {
            Common.currentUser.setTable(restaurantTable);
            loadMenu(restaurantId);
        }
    }

    private void loadMenu(String restaurantId) {
        adapter = new FirebaseRecyclerAdapter<Category,
                MenuViewHolder>(Category.class, R.layout.menu_item, MenuViewHolder.class, category.orderByChild("RestId").equalTo(restaurantId)) {
            @Override
            protected void populateViewHolder(MenuViewHolder viewHolder, Category model, int i) {
                viewHolder.txtMenuName.setText(model.getName());
                Picasso.with(getBaseContext()).load(model.getImage()).into(viewHolder.imageView);

                final Category clickItem = model;
                viewHolder.setItemClickListener(new ItemClickListener() {
                    @Override
                    public void onClick(View view, int position, boolean isLongClick){
                        // get categoryid and send to new activity
                        Intent foodList = new Intent(Home.this, FoodList.class);
                        foodList.putExtra("CategoryId", adapter.getRef(position).getKey());
                        startActivity(foodList);
                    }
                });
            }
        };
        recycler_menu.setAdapter(adapter);
    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.home, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        if(item.getItemId() == R.id.refresh)
            loadMenu(restaurantId);

        return super.onOptionsItemSelected(item);
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.nav_menu) {

        } else if (id == R.id.nav_cart) {
            Intent cartIntent = new Intent(Home.this,Cart.class);
            startActivity(cartIntent);

        } else if (id == R.id.nav_orders) {
            Intent orderIntent = new Intent(Home.this,OrderStatus.class);
            startActivity(orderIntent);

        } else if (id == R.id.nav_log_out) {
            Intent signIn = new Intent(Home.this,SignIn.class);
            signIn.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
            startActivity(signIn);

        }

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }
}
