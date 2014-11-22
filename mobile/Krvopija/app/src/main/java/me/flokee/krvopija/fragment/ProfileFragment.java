package me.flokee.krvopija.fragment;

import android.app.Fragment;
import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.*;
import com.afollestad.materialdialogs.MaterialDialog;
import me.flokee.krvopija.*;

import java.util.ArrayList;
import java.util.List;

public class ProfileFragment extends Fragment {

    @Override
    public View onCreateView(final LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.fragment_profile, container, false);
        String text = String.format("Profile Overview");
        getActivity().setTitle(text);

        ListView mListView = (ListView) rootView.findViewById(R.id.my_list_view);
        mListView.setItemsCanFocus(false);

        List<ProfileItem> profileItemList = new ArrayList<ProfileItem>();
        profileItemList.add(new ProfileItem(R.drawable.ic_attach_file_black_48dp, "test 1"));
        profileItemList.add(new ProfileItem(R.drawable.ic_attach_file_black_48dp, "test 2"));

        ProfileAdapter mAdapter = new ProfileAdapter(inflater.getContext(), profileItemList);
        mListView.setAdapter(mAdapter);

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
                        .build()
                        .show();
            }
        });

        return rootView;
    }

}
