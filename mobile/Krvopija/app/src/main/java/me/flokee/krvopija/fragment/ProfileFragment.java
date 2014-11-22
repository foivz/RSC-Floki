package me.flokee.krvopija.fragment;

import android.app.Fragment;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import me.flokee.krvopija.ProfileAdapter;
import me.flokee.krvopija.ProfileItem;
import me.flokee.krvopija.R;

import java.util.ArrayList;
import java.util.List;

public class ProfileFragment extends Fragment {

    private RecyclerView mRecyclerView;
    private RecyclerView.Adapter mAdapter;
    private RecyclerView.LayoutManager mLayoutManager;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.fragment_profile, container, false);
        String text = String.format("Profile Overview");
        getActivity().setTitle(text);

        mRecyclerView = (RecyclerView) rootView.findViewById(R.id.my_recycler_view);

        mLayoutManager = new LinearLayoutManager(inflater.getContext());
        mRecyclerView.setLayoutManager(mLayoutManager);

        List<ProfileItem> profileItemList = new ArrayList<ProfileItem>();
        profileItemList.add(new ProfileItem(R.drawable.ic_attach_file_black_48dp, "test 1"));
        profileItemList.add(new ProfileItem(R.drawable.ic_attach_file_black_48dp, "test 2"));

        mAdapter = new ProfileAdapter(inflater.getContext(), profileItemList);
        mRecyclerView.setAdapter(mAdapter);

        return rootView;
    }

}
