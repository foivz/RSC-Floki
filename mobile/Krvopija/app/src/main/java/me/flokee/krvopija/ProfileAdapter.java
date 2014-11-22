package me.flokee.krvopija;

import android.app.Activity;
import android.content.Context;
import android.provider.ContactsContract;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.List;

public class ProfileAdapter extends BaseAdapter {

    private List<ProfileItem> profileItems;
    private Context mContext;

    public ProfileAdapter(Context context, List<ProfileItem> profileItems) {
        this.mContext = context;
        this.profileItems = profileItems;
    }
    @Override
    public int getCount() {
        return profileItems.size();
    }

    @Override
    public Object getItem(int i) {
        return profileItems.get(i);
    }

    @Override
    public long getItemId(int i) {
        return i;
    }

    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {

        if(view == null) {
            LayoutInflater mInflater = (LayoutInflater) mContext
                    .getSystemService(Activity.LAYOUT_INFLATER_SERVICE);
            view = mInflater.inflate(R.layout.profile_list_item, null);
        }

        ImageView icon = (ImageView) view.findViewById(R.id.thumbnail);
        TextView text = (TextView) view.findViewById(R.id.text);

        ProfileItem profileItem = (ProfileItem) getItem(i);
        icon.setImageResource(profileItem.icon);
        text.setText(profileItem.text);

        return view;
    }

    @Override
    public boolean isEnabled(int position) {
        return false;
    }
}
