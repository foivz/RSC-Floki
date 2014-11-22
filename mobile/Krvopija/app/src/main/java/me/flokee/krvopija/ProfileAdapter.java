package me.flokee.krvopija;

import android.content.Context;
import android.provider.ContactsContract;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import java.util.List;

public class ProfileAdapter extends RecyclerView.Adapter<ProfileItemRowHolder> {

    private List<ProfileItem> profileItems;
    private Context mContext;

    public ProfileAdapter(Context context, List<ProfileItem> profileItems) {
        this.mContext = context;
        this.profileItems = profileItems;
    }

    @Override
    public ProfileItemRowHolder onCreateViewHolder(ViewGroup viewGroup, int i) {
        View v = LayoutInflater.from(viewGroup.getContext()).inflate(R.layout.profile_list_item, null);
        ProfileItemRowHolder pirh = new ProfileItemRowHolder(v);
        return pirh;
    }

    @Override
    public void onBindViewHolder(ProfileItemRowHolder feedListRowHolder, int i) {
        ProfileItem feedItem = profileItems.get(i);

        feedListRowHolder.text.setText(feedItem.text);
        feedListRowHolder.thumbnail.setImageResource(feedItem.icon);
    }

    @Override
    public int getItemCount() {
        return (null != profileItems ? profileItems.size() : 0);
    }
}
