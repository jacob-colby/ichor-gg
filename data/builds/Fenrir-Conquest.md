---
type: smite-build
god: Fenrir
mode: Conquest
builds:
- source: community
  aspect: Aspect of Loyalty
  aspect_pick_rate: 0.05
  aspect_win_rate: 1.0
  slot_order:
  - name: Tyrfing
    pick_rate: 0.55
    win_rate: 0.73
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.25
      win_rate: 0.8
    - name: The Reaper
      pick_rate: 0.1
      win_rate: 0.5
  - name: Bragi's Harp
    pick_rate: 0.35
    win_rate: 0.86
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.2
      win_rate: 0.75
    - name: Barbed Carver
      pick_rate: 0.15
      win_rate: 0.67
  - name: Magi's Cloak
    pick_rate: 0.16
    win_rate: 1.0
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.5
    - name: Jotunn's Revenge
      pick_rate: 0.11
      win_rate: 0.5
  - name: Sundering Echo
    pick_rate: 0.32
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.5
    - name: The Reaper
      pick_rate: 0.11
      win_rate: 0.5
  - name: Kinetic Cuirass
    pick_rate: 0.17
    win_rate: 0.67
    alternates:
    - name: Sundering Echo
      pick_rate: 0.11
      win_rate: 1.0
    - name: Spectral Armor
      pick_rate: 0.11
      win_rate: 0.5
  - name: The Reaper
    pick_rate: 0.22
    win_rate: 1.0
    alternates:
    - name: Plated Metal
      pick_rate: 0.11
      win_rate: 1.0
    - name: Blinking Abyss
      pick_rate: 0.11
      win_rate: 0.0
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.3
    win_rate: 0.83
  - name: Hunter's Cowl
    pick_rate: 0.2
    win_rate: 0.75
  - name: Leather Cowl
    pick_rate: 0.15
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/fenrir/
  last_verified: '2026-10-21'
  god_win_rate: 0.75
  god_matches_won: 15
  god_matches_played: 20
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-21'
  god_matches_analyzed: 814
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Crusher
  - Heartseeker
  - The Reaper
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Magi's Cloak — physical protection
    swap_item: Magi's Cloak
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Titan''s Bane, The Crusher, Heartseeker, Pendulum Blade, Hydra''s Lament,
    Avatar''s Parashu, Tekko-Kagi, Arondight, Transcendence, Runeforged Hammer, Avenging
    Blade, Golden Blade, Lernaean Bow, Shield Splitter, Dominance, Silverbranch Bow,
    Oath-Sworn Spear, Riptalon, Toxic Blade, Bloodforge, Deathbringer, Eye of the
    Storm, Damaru, Rage, Musashi''s Dual Swords, Sanguine Lash.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.77
      efficiency: 0.72
      win: 0.8
      pick: 0.25
      fit: 1.0
    Transcendence:
      total: 0.59
      efficiency: 0.53
      win: 0.73
      pick: 0.0
      fit: 0.52
    The Crusher:
      total: 0.64
      efficiency: 0.47
      win: 0.73
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.64
      efficiency: 0.47
      win: 0.73
      pick: 0.0
      fit: 1.0
    The Reaper:
      total: 0.79
      efficiency: 0.5
      win: 1.0
      pick: 0.68
      fit: 0.91
    Titan's Bane:
      total: 0.64
      efficiency: 0.47
      win: 0.73
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Heartseeker
  - The Reaper
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Magi's Cloak — magical protection
    swap_item: Magi's Cloak
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, Heartseeker, Titan''s Bane, The Crusher, Transcendence, Arondight, Pendulum
    Blade, Avatar''s Parashu, Runeforged Hammer, Tekko-Kagi, Avenging Blade, Dominance,
    Breastplate of Valor, Lernaean Bow, Genji''s Guard, Shield Splitter, Golden Blade,
    Oath-Sworn Spear, Daybreak Gavel, Silverbranch Bow, Bloodforge, Riptalon, Yogi''s
    Necklace, Toxic Blade, Deathbringer, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.73
      efficiency: 0.72
      win: 0.8
      pick: 0.25
      fit: 0.71
    Transcendence:
      total: 0.57
      efficiency: 0.53
      win: 0.73
      pick: 0.0
      fit: 0.39
    Hydra's Lament:
      total: 0.61
      efficiency: 0.54
      win: 0.73
      pick: 0.0
      fit: 0.63
    Heartseeker:
      total: 0.61
      efficiency: 0.47
      win: 0.73
      pick: 0.0
      fit: 0.77
    The Reaper:
      total: 0.73
      efficiency: 0.5
      win: 1.0
      pick: 0.68
      fit: 0.47
    Titan's Bane:
      total: 0.58
      efficiency: 0.47
      win: 0.73
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Pendulum Blade
  - The Reaper
  - Heartseeker
  flex_slots:
  - Pendulum Blade
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Magi's Cloak — magical protection
    swap_item: Magi's Cloak
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Heartseeker, Hydra''s Lament, Pendulum Blade, Titan''s Bane, The Crusher,
    Arondight, Avatar''s Parashu, Tekko-Kagi, Transcendence, Runeforged Hammer, Avenging
    Blade, Silverbranch Bow, Breastplate of Valor, Riptalon, Genji''s Guard, Lernaean
    Bow, Toxic Blade, Shield Splitter, Dominance, Daybreak Gavel, Golden Blade, Oath-Sworn
    Spear, Eye of Erebus, Screeching Gargoyle, Bloodforge, Chandra''s Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.74
      efficiency: 0.72
      win: 0.8
      pick: 0.25
      fit: 0.78
    Transcendence:
      total: 0.55
      efficiency: 0.53
      win: 0.73
      pick: 0.0
      fit: 0.22
    Hydra's Lament:
      total: 0.6
      efficiency: 0.54
      win: 0.73
      pick: 0.0
      fit: 0.54
    Pendulum Blade:
      total: 0.59
      efficiency: 0.42
      win: 0.73
      pick: 0.0
      fit: 0.78
    The Reaper:
      total: 0.74
      efficiency: 0.5
      win: 1.0
      pick: 0.68
      fit: 0.56
    Heartseeker:
      total: 0.61
      efficiency: 0.47
      win: 0.73
      pick: 0.0
      fit: 0.76
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Magi's Cloak
  - Kinetic Cuirass
  - Shifter's Shield
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Runeforged Hammer, Shield Splitter,
    Eye of the Storm, Berserker''s Shield, Erosion, Eye of Providence, Genji''s Guard,
    Breastplate of Valor, Draconic Scale, Yogi''s Necklace, Phoenix Feather, Avenging
    Blade, Heartseeker, Hydra''s Lament, Stone of Binding, Midgardian Mail, Chandra''s
    Grace, Titan''s Bane, Daybreak Gavel, Hide of the Nemean Lion, The Crusher, Leviathan''s
    Hide.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.69
      efficiency: 0.72
      win: 0.8
      pick: 0.25
      fit: 0.44
    Magi's Cloak:
      total: 0.7
      efficiency: 0.53
      win: 1.0
      pick: 0.25
      fit: 0.34
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.67
      pick: 0.37
      fit: 0.66
    Shifter's Shield:
      total: 0.63
      efficiency: 0.55
      win: 0.75
      pick: 0.27
      fit: 0.56
    The Reaper:
      total: 0.76
      efficiency: 0.5
      win: 1.0
      pick: 0.68
      fit: 0.7
    Amanita Charm:
      total: 0.69
      efficiency: 0.65
      win: 0.73
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Jotunn's Revenge
  - Magi's Cloak
  - Kinetic Cuirass
  - Shifter's Shield
  - The Reaper
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  - The Reaper
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Heartseeker
  - Avatar's Parashu
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Titan''s Bane, The Crusher, Heartseeker, Avatar''s Parashu, Pendulum
    Blade, Tekko-Kagi, Avenging Blade, Hydra''s Lament, Silverbranch Bow, Riptalon,
    Oath-Sworn Spear, Transcendence, Arondight, Toxic Blade, Runeforged Hammer, Lernaean
    Bow, Shield Splitter, Dominance, Golden Blade, Screeching Gargoyle, Daybreak Gavel,
    Bloodforge, Breastplate of Valor, Genji''s Guard, Deathbringer, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.77
      efficiency: 0.72
      win: 0.8
      pick: 0.25
      fit: 1.0
    The Crusher:
      total: 0.64
      efficiency: 0.47
      win: 0.73
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.64
      efficiency: 0.47
      win: 0.73
      pick: 0.0
      fit: 1.0
    The Reaper:
      total: 0.8
      efficiency: 0.5
      win: 1.0
      pick: 0.68
      fit: 0.94
    Titan's Bane:
      total: 0.64
      efficiency: 0.47
      win: 0.73
      pick: 0.0
      fit: 1.0
    Avatar's Parashu:
      total: 0.63
      efficiency: 0.45
      win: 0.73
      pick: 0.0
      fit: 0.94
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - The Reaper
  - Tekko-Kagi
  flex_slots:
  - Silverbranch Bow
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Riptalon, Silverbranch Bow, Tekko-Kagi, Lernaean Bow, Golden Blade,
    Toxic Blade, Heartseeker, Dominance, Qin''s Blade, Hydra''s Lament, Titan''s Bane,
    The Crusher, Sun Beam Bow, Transcendence, Berserker''s Shield, Avatar''s Parashu,
    Dagger of Frenzy, Arondight, Runeforged Hammer, Pendulum Blade, Avenging Blade,
    Vital Amplifier, Hastened Fatalis, Bloodforge, The Executioner, Odysseus'' Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.72
      win: 0.8
      pick: 0.25
      fit: 0.37
    Tyrfing:
      total: 0.64
      efficiency: 0.48
      win: 0.73
      pick: 0.55
      fit: 0.79
    Riptalon:
      total: 0.63
      efficiency: 0.51
      win: 0.73
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.62
      efficiency: 0.53
      win: 0.73
      pick: 0.0
      fit: 0.69
    The Reaper:
      total: 0.74
      efficiency: 0.55
      win: 1.0
      pick: 0.68
      fit: 0.44
    Tekko-Kagi:
      total: 0.6
      efficiency: 0.49
      win: 0.73
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Pendulum Blade
  - The Reaper
  - Heartseeker
  flex_slots:
  - Arondight
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Pendulum Blade, Arondight,
    Heartseeker, Breastplate of Valor, Genji''s Guard, Titan''s Bane, The Crusher,
    Avatar''s Parashu, Eye of Erebus, Transcendence, Screeching Gargoyle, Runeforged
    Hammer, Chandra''s Grace, Tekko-Kagi, Avenging Blade, Shield of the Phoenix, Silverbranch
    Bow, Daybreak Gavel, Lernaean Bow, Riptalon, Gladiator''s Shield, Shield Splitter,
    Dominance, Golden Blade, Prophetic Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.75
      efficiency: 0.72
      win: 0.8
      pick: 0.25
      fit: 0.85
    Hydra's Lament:
      total: 0.63
      efficiency: 0.54
      win: 0.73
      pick: 0.0
      fit: 0.75
    Arondight:
      total: 0.6
      efficiency: 0.5
      win: 0.73
      pick: 0.0
      fit: 0.65
    Pendulum Blade:
      total: 0.6
      efficiency: 0.42
      win: 0.73
      pick: 0.0
      fit: 0.85
    The Reaper:
      total: 0.71
      efficiency: 0.5
      win: 1.0
      pick: 0.68
      fit: 0.35
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.73
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Pendulum Blade
  - The Crusher
  - The Reaper
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Pendulum Blade
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
    Underrated for this god: Titan''s Bane, The Crusher, Heartseeker, Pendulum Blade,
    Hydra''s Lament, Avatar''s Parashu, Tekko-Kagi, Arondight, Transcendence, Runeforged
    Hammer, Avenging Blade, Golden Blade, Lernaean Bow, Shield Splitter, Dominance,
    Silverbranch Bow, Oath-Sworn Spear, Riptalon, Toxic Blade, Bloodforge, Deathbringer,
    Eye of the Storm, Damaru, Rage, Musashi''s Dual Swords, Sanguine Lash.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.77
      efficiency: 0.72
      win: 0.8
      pick: 0.25
      fit: 1.0
    Pendulum Blade:
      total: 0.63
      efficiency: 0.42
      win: 0.73
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.64
      efficiency: 0.47
      win: 0.73
      pick: 0.0
      fit: 1.0
    The Reaper:
      total: 0.79
      efficiency: 0.5
      win: 1.0
      pick: 0.68
      fit: 0.91
    Heartseeker:
      total: 0.64
      efficiency: 0.47
      win: 0.73
      pick: 0.0
      fit: 1.0
    Titan's Bane:
      total: 0.64
      efficiency: 0.47
      win: 0.73
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  starter: *id001
---
