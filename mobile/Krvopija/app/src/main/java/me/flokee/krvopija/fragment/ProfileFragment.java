package me.flokee.krvopija.fragment;

import android.app.Fragment;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;
import me.flokee.krvopija.MainActivity;
import me.flokee.krvopija.ProfileAdapter;
import me.flokee.krvopija.ProfileItem;
import me.flokee.krvopija.R;

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

        return rootView;
    }

}
