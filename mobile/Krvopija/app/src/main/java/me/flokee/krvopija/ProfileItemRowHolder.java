package me.flokee.krvopija;

import android.support.v7.widget.RecyclerView;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

public class ProfileItemRowHolder extends RecyclerView.ViewHolder {

    protected ImageView thumbnail;
    protected TextView text;

    public ProfileItemRowHolder(View view) {
        super(view);
        this.thumbnail = (ImageView) view.findViewById(R.id.thumbnail);
        this.text = (TextView) view.findViewById(R.id.text);
    }
}
