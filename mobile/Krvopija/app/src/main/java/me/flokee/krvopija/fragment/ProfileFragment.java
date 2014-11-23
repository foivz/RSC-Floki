package me.flokee.krvopija.fragment;

import android.app.Fragment;
import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.*;

import com.afollestad.materialdialogs.MaterialDialog;
import me.flokee.krvopija.*;
import me.flokee.krvopija.ProfileUpdateResponseObject;
import retrofit.Callback;
import retrofit.RetrofitError;
import retrofit.client.Response;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ProfileFragment extends Fragment {

    private static final String TAG =  ProfileFragment.class.getSimpleName();

    @Override
    public View onCreateView(final LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.fragment_profile, container, false);
        final String text = String.format("Profile Overview");
        getActivity().setTitle(text);

        final String token = ((MainActivity) getActivity()).getToken();

        final ListView mListView = (ListView) rootView.findViewById(R.id.my_list_view);
        mListView.setItemsCanFocus(false);

        Services.getKrvopijaService().profile(token, new Callback<ProfileResponseObject>() {
            @Override
            public void success(ProfileResponseObject profileResponseObject, Response response) {
                Log.i(TAG, "done");
                List<ProfileItem> profileItemList = new ArrayList<ProfileItem>();
                profileItemList.add(new ProfileItem(R.drawable.ic_attach_file_black_48dp, "" + profileResponseObject.getProfile().getNumDonations() + " donations"));
                profileItemList.add(new ProfileItem(R.drawable.ic_attach_file_black_48dp, "Blood type: " + profileResponseObject.getProfile().getBloodType().getAB0() + profileResponseObject.getProfile().getBloodType().getRH()));
                for(String achievement : profileResponseObject.getProfile().getAchivements()) {
                    profileItemList.add(new ProfileItem(R.drawable.ic_star_grey600_48dp, achievement));
                }

                ProfileAdapter mAdapter = new ProfileAdapter(inflater.getContext(), profileItemList);
                mListView.setAdapter(mAdapter);
            }

            @Override
            public void failure(RetrofitError error) {

            }
        });

        rootView.findViewById(R.id.add_icon).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                View view = inflater.inflate(R.layout.sick_view, null);
                Spinner spinner = (Spinner) view.findViewById(R.id.sick_spinner);
                // Create an ArrayAdapter using the string array and a default spinner layout
                ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(inflater.getContext(),
                                R.array.sicks_array, R.layout.spinner_sickness);
                // Specify the layout to use when the list of choices appears
                                adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
                // Apply the adapter to the spinner
                                spinner.setAdapter(adapter);

                new MaterialDialog.Builder(inflater.getContext())
                        .title("New donor issue")
                        .customView(view)
                        .positiveText("Add")
                        .positiveColor(Color.parseColor("#03a9f4"))
                        .callback(new MaterialDialog.SimpleCallback() {
                            @Override
                            public void onPositive(MaterialDialog materialDialog) {
                                String type = ((Spinner)materialDialog.getCustomView().findViewById(R.id.sick_spinner)).getSelectedItem().toString();

                                Services.getKrvopijaService().addEvent(token, type, new Callback<EventResponseObject>() {
                                    @Override
                                    public void success(EventResponseObject profileResponseObject, Response response) {
                                        Log.i("rest", "add issue with status " + profileResponseObject.getStatus());
                                        Toast.makeText(inflater.getContext(), "Update " + profileResponseObject.getStatus(), Toast.LENGTH_LONG);
                                    }

                                    @Override
                                    public void failure(RetrofitError error) {
                                        Log.e("rest", "failed to add issue " + error.getMessage());
                                    }
                                });
                            }
                        })
                        .build()
                        .show();
            }
        });

        rootView.findViewById(R.id.edit_icon).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                View view = inflater.inflate(R.layout.profile_edit_view, null);

                new MaterialDialog.Builder(inflater.getContext())
                        .title("Donor profile")
                        .customView(view)
                        .positiveText("Update")
                        .positiveColor(Color.parseColor("#03a9f4"))
                        .callback(new MaterialDialog.SimpleCallback() {
                            @Override
                            public void onPositive(MaterialDialog materialDialog) {
                                final String N = "\"";
                                String data = "{\"name\":"+N+((TextView)materialDialog.getCustomView().findViewById(R.id.editText)).getText().toString()+N+",";
                                data = data + "\"surname\":"+N+((TextView)materialDialog.getCustomView().findViewById(R.id.editText2)).getText().toString()+N+",";
                                data = data + "\"country\":"+N+((TextView)materialDialog.getCustomView().findViewById(R.id.editText3)).getText().toString()+N+"}";

                                Services.getKrvopijaService().updateProfile(token, data, new Callback<ProfileUpdateResponseObject>() {
                                    @Override
                                    public void success(ProfileUpdateResponseObject profileResponseObject, Response response) {
                                        Log.i("rest", "update profile with status " + profileResponseObject.getStatus());
                                        Toast.makeText(inflater.getContext(), "Update " + profileResponseObject.getStatus(), Toast.LENGTH_LONG);
                                    }

                                    @Override
                                    public void failure(RetrofitError error) {
                                        Log.e("rest", "failed to update profile " + error.getMessage());
                                    }
                                });
                            }
                        })
                        .build()
                        .show();
            }
        });

        return rootView;
    }

}
