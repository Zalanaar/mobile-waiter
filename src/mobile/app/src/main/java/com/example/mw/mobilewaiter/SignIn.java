package com.example.mw.mobilewaiter;

import android.app.ProgressDialog;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.example.mw.mobilewaiter.Common.Common;
import com.example.mw.mobilewaiter.Model.User;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.rengwuxian.materialedittext.MaterialEditText;
import com.google.zxing.integration.android.IntentIntegrator;
import com.google.zxing.integration.android.IntentResult;

public class SignIn extends AppCompatActivity {

    EditText edtPhone, edtPassword;
    Button btnSignIn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sign_in);

        edtPassword = (MaterialEditText)findViewById(R.id.edtPassword);
        edtPhone = (MaterialEditText)findViewById(R.id.edtPhone);
        btnSignIn = (Button)findViewById(R.id.btnSignIn);

        // Init Firebase
        FirebaseDatabase database = FirebaseDatabase.getInstance();
        final DatabaseReference table_user = database.getReference("User");

        btnSignIn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (Common.isConnectedToInternet(getBaseContext())) {

                    final ProgressDialog mDialog = new ProgressDialog(SignIn.this);
                    mDialog.setMessage("Please waiting...");
                    mDialog.show();

                    table_user.addValueEventListener(new ValueEventListener() {
                        @Override
                        public void onDataChange(DataSnapshot dataSnapshot) {

                            //check user in db
                            if (dataSnapshot.child(edtPhone.getText().toString()).exists()) {
                                //get user info
                                mDialog.dismiss();
                                User user = dataSnapshot.child(edtPhone.getText().toString()).getValue(User.class);
                                user.setPhone(edtPhone.getText().toString());  //set phone
                                if (user.getPassword().equals(edtPassword.getText().toString())) {

                                    Common.currentUser = user;
                                    IntentIntegrator barcodeScanner = new IntentIntegrator(SignIn.this);
                                    barcodeScanner.setOrientationLocked(false);
                                    barcodeScanner.initiateScan();


                                } else {
                                    Toast.makeText(SignIn.this, "Wrong password !", Toast.LENGTH_SHORT).show();

                                }
                            } else {
                                mDialog.dismiss();
                                Toast.makeText(SignIn.this, "User not exist in DB!", Toast.LENGTH_SHORT).show();

                            }
                        }

                        @Override
                        public void onCancelled(DatabaseError databaseError) {

                        }
                    });
                }
                else
                {
                    Toast.makeText(SignIn.this, "Please check your connection!", Toast.LENGTH_SHORT).show();
                    return;
                }
            }

        });

    }

    // Get the results:
     @Override
     protected void onActivityResult(int requestCode, int resultCode, Intent data) {
                IntentResult result = IntentIntegrator.parseActivityResult(requestCode, resultCode, data);
                if(result != null) {
                        if(result.getContents() == null) {
                                Toast.makeText(this, "Cancelled", Toast.LENGTH_LONG).show();
                            } else {
                                //Toast.makeText(this, "Scanned: " + result.getContents(), Toast.LENGTH_LONG).show();
                                        Intent home = new Intent(this, Home.class);
                                home.putExtra("RestaurantId", result.getContents());
                                startActivity(home);
                                finish();
                            }
                    } else {
                        super.onActivityResult(requestCode, resultCode, data);
                    }
            }
}
