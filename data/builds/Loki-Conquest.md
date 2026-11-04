---
type: smite-build
god: Loki
mode: Conquest
builds:
- source: community
  aspect: Aspect of Agony
  aspect_pick_rate: 1.0
  aspect_win_rate: 0.5
  slot_order:
  - name: Shifter's Shield
    pick_rate: 1.0
    win_rate: 0.5
  - name: Wyrmskin Hide
    pick_rate: 1.0
    win_rate: 0.5
  - name: Hussar's Wings
    pick_rate: 0.5
    win_rate: 1.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.5
      win_rate: 0.0
  - name: Sundering Echo
    pick_rate: 0.5
    win_rate: 0.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.5
      win_rate: 1.0
  - name: Brawler’s Beat Stick
    pick_rate: 0.5
    win_rate: 0.0
    alternates:
    - name: Sundering Echo
      pick_rate: 0.5
      win_rate: 1.0
  - name: Ancile
    pick_rate: 1.0
    win_rate: 0.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 1.0
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/loki/
  last_verified: '2026-11-04'
  god_win_rate: 0.5
  god_matches_won: 1
  god_matches_played: 2
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-04'
  god_matches_analyzed: 149
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Freya's Tears
  - Tekko-Kagi
  - The Crusher
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Hussar's Wings — magical protection
    swap_item: Hussar's Wings
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Titan''s Bane, The Crusher, The Reaper, Tekko-Kagi,
    Heartseeker, Hydra''s Lament, Pendulum Blade, Avatar''s Parashu, Tyrfing, Arondight,
    Transcendence, Runeforged Hammer, Golden Blade, Avenging Blade, Shield Splitter,
    Eye of the Storm, Silverbranch Bow, Dominance, Bloodforge, Lernaean Bow, Toxic
    Blade, Oath-Sworn Spear, Barbed Carver, Riptalon, Rage, Musashi''s Dual Swords,
    Deathbringer, Damaru, Sanguine Lash.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Reaper:
      total: 0.54
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.91
    Freya's Tears:
      total: 0.62
      efficiency: 0.34
      win: 1.0
      pick: 0.83
      fit: 0.09
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.91
    The Crusher:
      total: 0.55
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 1.0
    Titan's Bane:
      total: 0.56
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Freya's Tears
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Freya's Tears
  - Titan's Bane
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Hydra''s Lament, Titan''s Bane, Heartseeker, The Crusher, Arondight,
    The Reaper, Transcendence, Tekko-Kagi, Pendulum Blade, Tyrfing, Avatar''s Parashu,
    Runeforged Hammer, Dominance, Avenging Blade, Shield Splitter, Eye of the Storm,
    Genji''s Guard, Bloodforge, Lernaean Bow, Golden Blade, Damaru, Breastplate of
    Valor, Chandra''s Grace, Oath-Sworn Spear, Silverbranch Bow, Barbed Carver, Yogi''s
    Necklace, Toxic Blade, Rage.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.71
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.39
    Hydra's Lament:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.63
      efficiency: 0.34
      win: 1.0
      pick: 0.83
      fit: 0.14
    Titan's Bane:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.57
    Heartseeker:
      total: 0.49
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Freya's Tears
  - The Crusher
  - Titan's Bane
  flex_slots:
  - The Crusher
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Titan''s Bane, Hydra''s Lament, The Crusher, Heartseeker,
    The Reaper, Pendulum Blade, Arondight, Tekko-Kagi, Avatar''s Parashu, Tyrfing,
    Transcendence, Runeforged Hammer, Silverbranch Bow, Damaru, Avenging Blade, Genji''s
    Guard, Toxic Blade, Shield Splitter, Eye of the Storm, Dominance, Breastplate
    of Valor, Golden Blade, Bloodforge, Lernaean Bow, Chandra''s Grace, Riptalon,
    Oath-Sworn Spear, Barbed Carver, Eye of Erebus.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.78
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.22
    Hydra's Lament:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.54
    Freya's Tears:
      total: 0.64
      efficiency: 0.34
      win: 1.0
      pick: 0.83
      fit: 0.22
    The Crusher:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.66
    Titan's Bane:
      total: 0.51
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shifter's Shield
  - Wyrmskin Hide
  - Hussar's Wings
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Wyrmskin Hide
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield Splitter,
    Berserker''s Shield, Shield of the Phoenix, The Reaper, Runeforged Hammer, Genji''s
    Guard, Phoenix Feather, Yogi''s Necklace, Titan''s Bane, Erosion, Eye of Providence,
    Oni Hunter''s Garb, Draconic Scale, Avenging Blade, Breastplate of Valor, Midgardian
    Mail, Hydra''s Lament, The Crusher, Leviathan''s Hide, Chandra''s Grace, Stone
    of Binding, Heartseeker, Magi''s Cloak, Golden Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.44
    Shifter's Shield:
      total: 0.52
      efficiency: 0.47
      win: 0.5
      pick: 1.0
      fit: 0.56
    Wyrmskin Hide:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 1.0
      fit: 0.62
    Hussar's Wings:
      total: 0.71
      efficiency: 0.38
      win: 1.0
      pick: 0.78
      fit: 0.56
    Freya's Tears:
      total: 0.75
      efficiency: 0.58
      win: 1.0
      pick: 0.83
      fit: 0.38
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Shifter's Shield
  - Wyrmskin Hide
  - Hussar's Wings
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Freya's Tears
  - Tekko-Kagi
  - The Crusher
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Hussar's Wings — magical protection
    swap_item: Hussar's Wings
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Titan''s Bane, The Crusher, The Reaper, Tekko-Kagi,
    Heartseeker, Avatar''s Parashu, Pendulum Blade, Hydra''s Lament, Avenging Blade,
    Silverbranch Bow, Toxic Blade, Tyrfing, Arondight, Oath-Sworn Spear, Transcendence,
    Riptalon, Runeforged Hammer, Shield Splitter, Eye of the Storm, Golden Blade,
    Dominance, Bloodforge, Lernaean Bow, Barbed Carver, Screeching Gargoyle, Damaru,
    Genji''s Guard, Rage, Musashi''s Dual Swords.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Reaper:
      total: 0.55
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.94
    Freya's Tears:
      total: 0.62
      efficiency: 0.34
      win: 1.0
      pick: 0.83
      fit: 0.06
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.94
    The Crusher:
      total: 0.55
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 1.0
    Titan's Bane:
      total: 0.56
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Freya's Tears
  - Tekko-Kagi
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Silverbranch Bow
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Tyrfing, Tekko-Kagi, Jotunn''s Revenge, Silverbranch Bow, Riptalon,
    Golden Blade, Lernaean Bow, Toxic Blade, The Reaper, Titan''s Bane, Dominance,
    Qin''s Blade, Hydra''s Lament, The Crusher, Heartseeker, Sun Beam Bow, Arondight,
    Berserker''s Shield, Bloodforge, Transcendence, Dagger of Frenzy, Runeforged Hammer,
    Avatar''s Parashu, Pendulum Blade, Avenging Blade, Barbed Carver, Vital Amplifier,
    Hastened Fatalis, Shield Splitter, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.37
    Tyrfing:
      total: 0.52
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.79
    Freya's Tears:
      total: 0.62
      efficiency: 0.34
      win: 1.0
      pick: 0.83
      fit: 0.04
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.65
    Riptalon:
      total: 0.5
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Freya's Tears
  - Hussar's Wings
  - Pendulum Blade
  flex_slots:
  - Pendulum Blade
  - Hussar's Wings
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Hydra''s Lament,
    Arondight, Pendulum Blade, Titan''s Bane, Damaru, Genji''s Guard, The Crusher,
    Heartseeker, The Reaper, Breastplate of Valor, Chandra''s Grace, Tekko-Kagi, Tyrfing,
    Transcendence, Avatar''s Parashu, Eye of Erebus, Screeching Gargoyle, Runeforged
    Hammer, Avenging Blade, Silverbranch Bow, Shield Splitter, Shield of the Phoenix,
    Eye of the Storm, Toxic Blade, Dominance, Golden Blade, Bloodforge, Lernaean Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.85
    Hydra's Lament:
      total: 0.53
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.75
    Arondight:
      total: 0.51
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.65
    Freya's Tears:
      total: 0.69
      efficiency: 0.34
      win: 1.0
      pick: 0.83
      fit: 0.5
    Hussar's Wings:
      total: 0.49
      efficiency: 0.0
      win: 1.0
      pick: 0.78
      fit: 0.0
    Pendulum Blade:
      total: 0.5
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Freya's Tears
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Tekko-Kagi
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Titan''s Bane, The Crusher, The Reaper,
    Tekko-Kagi, Heartseeker, Hydra''s Lament, Pendulum Blade, Avatar''s Parashu, Tyrfing,
    Arondight, Transcendence, Runeforged Hammer, Golden Blade, Avenging Blade, Shield
    Splitter, Eye of the Storm, Silverbranch Bow, Dominance, Bloodforge, Lernaean
    Bow, Toxic Blade, Oath-Sworn Spear, Barbed Carver, Riptalon, Rage, Musashi''s
    Dual Swords, Deathbringer, Damaru, Sanguine Lash.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 1.0
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.52
    The Reaper:
      total: 0.54
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.91
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.91
    The Crusher:
      total: 0.55
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 1.0
    Titan's Bane:
      total: 0.56
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
---
