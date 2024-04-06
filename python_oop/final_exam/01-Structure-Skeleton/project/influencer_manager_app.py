from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCERS = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}
    VALID_CAMPAIGNS = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCERS:
            return f"{influencer_type} is not an allowed influencer type."

        try:
            influencer = [i for i in self.influencers if i.username == username][0]
            return f"{username} is already registered."
        except IndexError:
            new_influencer = self.VALID_INFLUENCERS[influencer_type](username, followers, engagement_rate)
            self.influencers.append(new_influencer)
            return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGNS:
            return f"{campaign_type} is not a valid campaign type."

        try:
            campaign = [c for c in self.campaigns if c.campaign_id == campaign_id][0]
            return f"Campaign ID {campaign_id} has already been created."
        except IndexError:
            new_campaign = self.VALID_CAMPAIGNS[campaign_type](brand, required_engagement)
            self.campaigns.append(new_campaign)
            return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        try:
            influencer = [i for i in self.influencers if i.username == influencer_username][0]
        except IndexError:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaign = [c for c in self.campaigns if c.campaign_id == campaign_id][0]
        except IndexError:
            return f"Campaign with ID {campaign_id} not found."

        if not influencer.check_eligibility(campaign.required_engagement):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        payment = influencer.calculate_payment(campaign)
        if payment > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        total_reached_followers = {}

        for campaign in self.campaigns:
            reached_followers = 0

            for influencer in campaign.approved_influencers:
                reached_followers += influencer.reached_followers(type(campaign).__name__)

            if reached_followers > 0:
                total_reached_followers[campaign] = reached_followers

        return total_reached_followers

    def influencer_campaign_report(self, username: str):
        influencer = [i for i in self.influencers if i.username == username][0]
        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        def campaign_statistics(self):
            sorted_campaigns = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))

            statistics = ["$$ Campaign Statistics $$"]

            for campaign in sorted_campaigns:
                brand = campaign.brand
                approved_influencers = len(campaign.approved_influencers)
                total_budget = f"${campaign.budget:.2f}"
                total_reached_followers = sum(influencer.reached_followers(type(campaign).__name__) for influencer in
                                              campaign.approved_influencers)

                statistics.append(
                    f"  * Brand: {brand}, Total influencers: {approved_influencers}, Total budget: {total_budget}, Total reached followers: {total_reached_followers}")

            return "\n".join(statistics)

