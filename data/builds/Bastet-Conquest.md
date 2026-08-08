---
type: smite-build
god: Bastet
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Watchful Pride
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.51
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.71
    win_rate: 0.55
    alternates:
    - name: Transcendence
      pick_rate: 0.12
      win_rate: 0.58
    - name: Shifter's Shield
      pick_rate: 0.05
      win_rate: 0.6
  - name: Transcendence
    pick_rate: 0.3
    win_rate: 0.57
    alternates:
    - name: Barbed Carver
      pick_rate: 0.19
      win_rate: 0.54
    - name: Jotunn's Revenge
      pick_rate: 0.14
      win_rate: 0.55
  - name: Barbed Carver
    pick_rate: 0.2
    win_rate: 0.57
    alternates:
    - name: The Reaper
      pick_rate: 0.15
      win_rate: 0.57
    - name: Pendulum Blade
      pick_rate: 0.11
      win_rate: 0.54
  - name: Heartseeker
    pick_rate: 0.3
    win_rate: 0.57
    alternates:
    - name: Titan's Bane
      pick_rate: 0.17
      win_rate: 0.54
    - name: The Crusher
      pick_rate: 0.08
      win_rate: 0.51
  - name: Titan's Bane
    pick_rate: 0.18
    win_rate: 0.66
    alternates:
    - name: Heartseeker
      pick_rate: 0.2
      win_rate: 0.59
    - name: Lucerne Hammer
      pick_rate: 0.09
      win_rate: 0.5
  - name: Lucerne Hammer
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.53
    - name: Skeggox
      pick_rate: 0.06
      win_rate: 0.61
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.32
    win_rate: 0.62
  - name: Bluestone Pendant
    pick_rate: 0.19
    win_rate: 0.52
  - name: Bumba's Hammer
    pick_rate: 0.09
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/bastet/
  last_verified: '2026-08-08'
  god_win_rate: 0.5487944890929966
  god_matches_won: 478
  god_matches_played: 871
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-08'
  god_matches_analyzed: 14443
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Pendulum Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, The Reaper, Pendulum Blade, Hydra''s Lament, Runeforged
    Hammer, Tekko-Kagi, Lernaean Bow, Avatar''s Parashu, Damaru, Avenging Blade, Golden
    Blade, Arondight, Genji''s Guard, Shield Splitter, Dominance, Eye of the Storm,
    Tyrfing, Riptalon, Silverbranch Bow, Berserker''s Shield, Breastplate of Valor,
    Bloodforge, Musashi''s Dual Swords, Amanita Charm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.65
      win: 0.55
      pick: 0.71
      fit: 1.0
    The Reaper:
      total: 0.59
      efficiency: 0.53
      win: 0.57
      pick: 0.15
      fit: 0.91
    Pendulum Blade:
      total: 0.55
      efficiency: 0.42
      win: 0.54
      pick: 0.11
      fit: 1.0
    The Crusher:
      total: 0.61
      efficiency: 0.65
      win: 0.51
      pick: 0.08
      fit: 1.0
    Heartseeker:
      total: 0.58
      efficiency: 0.46
      win: 0.57
      pick: 0.3
      fit: 1.0
    Titan's Bane:
      total: 0.6
      efficiency: 0.46
      win: 0.66
      pick: 0.18
      fit: 0.91
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Hydra's Lament
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Crusher, The Reaper, Hydra''s Lament, Pendulum Blade, Genji''s Guard,
    Breastplate of Valor, Runeforged Hammer, Berserker''s Shield, Riptalon, Tekko-Kagi,
    Lernaean Bow, Arondight, Damaru, Silverbranch Bow, Freya''s Tears, Shield of the
    Phoenix, Avatar''s Parashu, Amanita Charm, Oni Hunter''s Garb, Avenging Blade,
    Golden Blade, Yogi''s Necklace, Kinetic Cuirass, Shield Splitter, Dominance, Screeching
    Gargoyle.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.65
      win: 0.55
      pick: 0.71
      fit: 0.78
    Hydra's Lament:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.53
      efficiency: 0.53
      win: 0.57
      pick: 0.15
      fit: 0.56
    The Crusher:
      total: 0.56
      efficiency: 0.65
      win: 0.51
      pick: 0.08
      fit: 0.66
    Heartseeker:
      total: 0.53
      efficiency: 0.46
      win: 0.57
      pick: 0.3
      fit: 0.66
    Titan's Bane:
      total: 0.55
      efficiency: 0.46
      win: 0.66
      pick: 0.18
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Reaper
  - Shifter's Shield
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, The Reaper, Shifter''s Shield, Kinetic Cuirass, The Crusher,
    Shield of the Phoenix, Berserker''s Shield, Eye of Providence, Runeforged Hammer,
    Oni Hunter''s Garb, Genji''s Guard, Eye of the Storm, Shield Splitter, Chandra''s
    Grace, Erosion, Hydra''s Lament, Phoenix Feather, Spectral Armor, Riptalon, Freya''s
    Tears, Avenging Blade, Draconic Scale, Breastplate of Valor, Pharaoh''s Curse,
    Golden Blade, Yogi''s Necklace, Leviathan''s Hide, Midgardian Mail.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.55
      pick: 0.71
      fit: 0.44
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.66
    The Reaper:
      total: 0.56
      efficiency: 0.53
      win: 0.57
      pick: 0.15
      fit: 0.7
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.6
      pick: 0.05
      fit: 0.56
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.51
      pick: 0.08
      fit: 0.5
    Amanita Charm:
      total: 0.59
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Pendulum Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, The Reaper, Pendulum Blade, Tekko-Kagi, Avatar''s Parashu,
    Avenging Blade, Riptalon, Hydra''s Lament, Silverbranch Bow, Runeforged Hammer,
    Genji''s Guard, Lernaean Bow, Damaru, Berserker''s Shield, Golden Blade, Toxic
    Blade, Screeching Gargoyle, Breastplate of Valor, Shield Splitter, Dominance,
    Arondight, Oath-Sworn Spear, Amanita Charm, Eye of the Storm, Tyrfing, Oni Hunter''s
    Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.65
      win: 0.55
      pick: 0.71
      fit: 1.0
    The Reaper:
      total: 0.59
      efficiency: 0.53
      win: 0.57
      pick: 0.15
      fit: 0.94
    Pendulum Blade:
      total: 0.55
      efficiency: 0.42
      win: 0.54
      pick: 0.11
      fit: 1.0
    The Crusher:
      total: 0.61
      efficiency: 0.65
      win: 0.51
      pick: 0.08
      fit: 1.0
    Heartseeker:
      total: 0.58
      efficiency: 0.46
      win: 0.57
      pick: 0.3
      fit: 1.0
    Titan's Bane:
      total: 0.61
      efficiency: 0.46
      win: 0.66
      pick: 0.18
      fit: 0.94
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Berserker's Shield
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, The Crusher, Golden Blade, Berserker''s Shield, Silverbranch
    Bow, The Reaper, Tyrfing, Lernaean Bow, Dominance, Tekko-Kagi, Hydra''s Lament,
    Genji''s Guard, Toxic Blade, Runeforged Hammer, Pharaoh''s Curse, Breastplate
    of Valor, Damaru, Shogun''s Ofuda, Amanita Charm, Oni Hunter''s Garb, Yogi''s
    Necklace, Eros'' Bow, Kinetic Cuirass, Qin''s Blade, Avenging Blade, Eye of Providence,
    Shield Splitter.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.69
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.55
      pick: 0.71
      fit: 0.37
    Riptalon:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.79
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.51
      pick: 0.08
      fit: 0.43
    Titan's Bane:
      total: 0.52
      efficiency: 0.46
      win: 0.66
      pick: 0.18
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Pendulum Blade
  - The Crusher
  flex_slots:
  - The Crusher
  - Pendulum Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Hydra''s Lament, Breastplate
    of Valor, The Crusher, Pendulum Blade, Freya''s Tears, The Reaper, Shield of the
    Phoenix, Arondight, Screeching Gargoyle, Chandra''s Grace, Berserker''s Shield,
    Runeforged Hammer, Gladiator''s Shield, Lernaean Bow, Amanita Charm, Damaru, Oni
    Hunter''s Garb, Yogi''s Necklace, Kinetic Cuirass, Riptalon, Prophetic Cloak,
    Silverbranch Bow, Avenging Blade, Regrowth Striders, Eye of Providence, Golden
    Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.5
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.65
      win: 0.55
      pick: 0.71
      fit: 0.85
    Hydra's Lament:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.75
    Pendulum Blade:
      total: 0.52
      efficiency: 0.42
      win: 0.54
      pick: 0.11
      fit: 0.85
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.51
      pick: 0.08
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Runeforged Hammer
  - The Reaper
  - The Crusher
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, The Reaper, Hydra''s Lament, Runeforged
    Hammer, Pendulum Blade, Tekko-Kagi, Lernaean Bow, Avatar''s Parashu, Damaru, Avenging
    Blade, Golden Blade, Arondight, Genji''s Guard, Shield Splitter, Dominance, Eye
    of the Storm, Tyrfing, Riptalon, Silverbranch Bow, Berserker''s Shield, Breastplate
    of Valor, Bloodforge, Musashi''s Dual Swords, Amanita Charm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.65
      win: 0.55
      pick: 0.71
      fit: 1.0
    Hydra's Lament:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.7
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.62
    The Reaper:
      total: 0.59
      efficiency: 0.53
      win: 0.57
      pick: 0.15
      fit: 0.91
    The Crusher:
      total: 0.61
      efficiency: 0.65
      win: 0.51
      pick: 0.08
      fit: 1.0
    Heartseeker:
      total: 0.58
      efficiency: 0.46
      win: 0.57
      pick: 0.3
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: The Crusher, The Reaper, Hydra''s
    Lament, Runeforged Hammer, Pendulum Blade, Tekko-Kagi, Lernaean Bow, Avatar''s
    Parashu, Damaru, Avenging Blade, Golden Blade, Arondight, Genji''s Guard, Shield
    Splitter, Dominance, Eye of the Storm, Tyrfing, Riptalon, Silverbranch Bow, Berserker''s
    Shield, Breastplate of Valor, Bloodforge, Musashi''s Dual Swords, Amanita Charm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.65
      win: 0.55
      pick: 0.71
      fit: 1.0
    Hydra's Lament:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.7
    The Reaper:
      total: 0.59
      efficiency: 0.53
      win: 0.57
      pick: 0.15
      fit: 0.91
    The Crusher:
      total: 0.61
      efficiency: 0.65
      win: 0.51
      pick: 0.08
      fit: 1.0
    Heartseeker:
      total: 0.58
      efficiency: 0.46
      win: 0.57
      pick: 0.3
      fit: 1.0
    Titan's Bane:
      total: 0.6
      efficiency: 0.46
      win: 0.66
      pick: 0.18
      fit: 0.91
  swaps:
  - added: Titan's Bane
    removed: Runeforged Hammer
    reason: community 66% win over 157 matches (vs 55% on this god), taking the model's
      weakest slot from Runeforged Hammer
  starter: *id001
---
