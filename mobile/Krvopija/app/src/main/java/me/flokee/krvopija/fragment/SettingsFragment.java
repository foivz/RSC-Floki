package me.flokee.krvopija.fragment;

import android.app.Fragment;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import me.flokee.krvopija.R;

public class SettingsFragment extends Fragment {

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.dummy_fragment, container, false);
        String text = String.format("Ja sam mali Settings");
        ((TextView) rootView.findViewById(R.id.textView)).setText(text);
        getActivity().setTitle(text);
        return rootView;
    }

}
