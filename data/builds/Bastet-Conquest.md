---
type: smite-build
god: Bastet
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Watchful Pride
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.33
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.69
    win_rate: 0.6
    alternates:
    - name: Transcendence
      pick_rate: 0.12
      win_rate: 0.4
    - name: Barbed Carver
      pick_rate: 0.06
      win_rate: 0.6
  - name: Pendulum Blade
    pick_rate: 0.2
    win_rate: 0.65
    alternates:
    - name: Transcendence
      pick_rate: 0.18
      win_rate: 0.73
    - name: Barbed Carver
      pick_rate: 0.14
      win_rate: 0.5
  - name: Barbed Carver
    pick_rate: 0.3
    win_rate: 0.67
    alternates:
    - name: The Crusher
      pick_rate: 0.18
      win_rate: 0.36
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.71
  - name: Heartseeker
    pick_rate: 0.38
    win_rate: 0.57
    alternates:
    - name: The Reaper
      pick_rate: 0.12
      win_rate: 0.89
    - name: The Crusher
      pick_rate: 0.06
      win_rate: 0.8
  - name: Titan's Bane
    pick_rate: 0.16
    win_rate: 0.42
    alternates:
    - name: Heartseeker
      pick_rate: 0.21
      win_rate: 0.67
    - name: Avatar's Parashu
      pick_rate: 0.07
      win_rate: 0.6
  - name: Skeggox
    pick_rate: 0.16
    win_rate: 0.86
    alternates:
    - name: Axe
      pick_rate: 0.16
      win_rate: 0.71
    - name: Lucerne Hammer
      pick_rate: 0.09
      win_rate: 0.5
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.36
    win_rate: 0.63
  - name: Bluestone Pendant
    pick_rate: 0.35
    win_rate: 0.48
  - name: Bumba's Cudgel
    pick_rate: 0.06
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/bastet/
  last_verified: '2026-09-24'
  god_win_rate: 0.5662650602409639
  god_matches_won: 47
  god_matches_played: 83
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-24'
  god_matches_analyzed: 1954
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Pendulum Blade
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Hydra's Lament
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Hydra''s Lament, Tekko-Kagi, Tyrfing, Arondight, Runeforged Hammer,
    Avenging Blade, Golden Blade, Silverbranch Bow, Lernaean Bow, Shield Splitter,
    Dominance, Riptalon, Oath-Sworn Spear, Toxic Blade, Bloodforge, Deathbringer,
    Eye of the Storm, Damaru, Rage, Musashi''s Dual Swords, Sanguine Lash.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.71
      efficiency: 0.72
      win: 0.6
      pick: 0.69
      fit: 1.0
    Transcendence:
      total: 0.6
      efficiency: 0.53
      win: 0.73
      pick: 0.25
      fit: 0.52
    Hydra's Lament:
      total: 0.58
      efficiency: 0.54
      win: 0.62
      pick: 0.0
      fit: 0.7
    The Reaper:
      total: 0.72
      efficiency: 0.5
      win: 0.89
      pick: 0.2
      fit: 0.91
    Pendulum Blade:
      total: 0.6
      efficiency: 0.42
      win: 0.65
      pick: 0.27
      fit: 1.0
    Heartseeker:
      total: 0.6
      efficiency: 0.47
      win: 0.57
      pick: 0.63
      fit: 1.0
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Pendulum Blade
  - Heartseeker
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Pendulum Blade
  - Heartseeker
  flex_slots:
  - Hydra's Lament
  - Pendulum Blade
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, Arondight, Tyrfing, Runeforged Hammer, Tekko-Kagi, Avenging Blade, Dominance,
    Breastplate of Valor, Lernaean Bow, Genji''s Guard, Shield Splitter, Golden Blade,
    Oath-Sworn Spear, Silverbranch Bow, Daybreak Gavel, Riptalon, Bloodforge, Yogi''s
    Necklace, Toxic Blade, Deathbringer, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.6
      pick: 0.69
      fit: 0.71
    Transcendence:
      total: 0.58
      efficiency: 0.53
      win: 0.73
      pick: 0.25
      fit: 0.39
    Hydra's Lament:
      total: 0.57
      efficiency: 0.54
      win: 0.62
      pick: 0.0
      fit: 0.63
    The Reaper:
      total: 0.65
      efficiency: 0.5
      win: 0.89
      pick: 0.2
      fit: 0.47
    Pendulum Blade:
      total: 0.55
      efficiency: 0.42
      win: 0.65
      pick: 0.27
      fit: 0.61
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.57
      pick: 0.63
      fit: 0.77
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Pendulum Blade
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Pendulum Blade
  - Heartseeker
  flex_slots:
  - Transcendence
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
    god: Hydra''s Lament, Arondight, Tekko-Kagi, Tyrfing, Runeforged Hammer, Silverbranch
    Bow, Avenging Blade, Breastplate of Valor, Riptalon, Genji''s Guard, Toxic Blade,
    Lernaean Bow, Shield Splitter, Dominance, Golden Blade, Daybreak Gavel, Oath-Sworn
    Spear, Eye of Erebus, Screeching Gargoyle, Bloodforge, Chandra''s Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.72
      win: 0.6
      pick: 0.69
      fit: 0.78
    Transcendence:
      total: 0.56
      efficiency: 0.53
      win: 0.73
      pick: 0.25
      fit: 0.22
    Hydra's Lament:
      total: 0.55
      efficiency: 0.54
      win: 0.62
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.67
      efficiency: 0.5
      win: 0.89
      pick: 0.2
      fit: 0.56
    Pendulum Blade:
      total: 0.57
      efficiency: 0.42
      win: 0.65
      pick: 0.27
      fit: 0.78
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.57
      pick: 0.63
      fit: 0.76
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Pendulum Blade
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Runeforged Hammer
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Runeforged Hammer,
    Shield Splitter, Shifter''s Shield, Eye of the Storm, Freya''s Tears, Berserker''s
    Shield, Erosion, Eye of Providence, Genji''s Guard, Breastplate of Valor, Draconic
    Scale, Yogi''s Necklace, Phoenix Feather, Avenging Blade, Stone of Binding, Hydra''s
    Lament, Midgardian Mail, Chandra''s Grace, Daybreak Gavel, Hide of the Nemean
    Lion, Magi''s Cloak, Leviathan''s Hide.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.6
      pick: 0.69
      fit: 0.44
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.66
    Transcendence:
      total: 0.56
      efficiency: 0.53
      win: 0.73
      pick: 0.25
      fit: 0.23
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.69
      efficiency: 0.5
      win: 0.89
      pick: 0.2
      fit: 0.7
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Pendulum Blade
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Avatar's Parashu
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    for this god: Tekko-Kagi, Avenging Blade, Hydra''s Lament, Silverbranch Bow, Riptalon,
    Tyrfing, Toxic Blade, Oath-Sworn Spear, Arondight, Runeforged Hammer, Golden Blade,
    Lernaean Bow, Shield Splitter, Dominance, Screeching Gargoyle, Daybreak Gavel,
    Bloodforge, Breastplate of Valor, Genji''s Guard, Deathbringer, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.71
      efficiency: 0.72
      win: 0.6
      pick: 0.69
      fit: 1.0
    Transcendence:
      total: 0.57
      efficiency: 0.53
      win: 0.73
      pick: 0.25
      fit: 0.32
    The Reaper:
      total: 0.73
      efficiency: 0.5
      win: 0.89
      pick: 0.2
      fit: 0.94
    Pendulum Blade:
      total: 0.6
      efficiency: 0.42
      win: 0.65
      pick: 0.27
      fit: 1.0
    Heartseeker:
      total: 0.6
      efficiency: 0.47
      win: 0.57
      pick: 0.63
      fit: 1.0
    Avatar's Parashu:
      total: 0.58
      efficiency: 0.45
      win: 0.6
      pick: 0.15
      fit: 0.94
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Pendulum Blade
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - The Reaper
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Silverbranch Bow
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    this god: Riptalon, Tyrfing, Silverbranch Bow, Tekko-Kagi, Lernaean Bow, Golden
    Blade, Toxic Blade, Dominance, Qin''s Blade, Hydra''s Lament, Sun Beam Bow, Berserker''s
    Shield, Dagger of Frenzy, Arondight, Runeforged Hammer, Avenging Blade, Vital
    Amplifier, Hastened Fatalis, Bloodforge, The Executioner, Odysseus'' Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.6
      pick: 0.69
      fit: 0.37
    Transcendence:
      total: 0.55
      efficiency: 0.53
      win: 0.73
      pick: 0.25
      fit: 0.17
    Tyrfing:
      total: 0.57
      efficiency: 0.48
      win: 0.62
      pick: 0.0
      fit: 0.79
    The Reaper:
      total: 0.67
      efficiency: 0.55
      win: 0.89
      pick: 0.2
      fit: 0.44
    Riptalon:
      total: 0.58
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Pendulum Blade
  - Arondight
  flex_slots:
  - Arondight
  - Transcendence
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
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Arondight, Breastplate
    of Valor, Genji''s Guard, Tyrfing, Eye of Erebus, Screeching Gargoyle, Runeforged
    Hammer, Chandra''s Grace, Freya''s Tears, Tekko-Kagi, Avenging Blade, Shield of
    the Phoenix, Silverbranch Bow, Daybreak Gavel, Riptalon, Lernaean Bow, Golden
    Blade, Gladiator''s Shield, Shield Splitter, Dominance, Toxic Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.72
      win: 0.6
      pick: 0.69
      fit: 0.85
    Transcendence:
      total: 0.55
      efficiency: 0.53
      win: 0.73
      pick: 0.25
      fit: 0.15
    Hydra's Lament:
      total: 0.58
      efficiency: 0.54
      win: 0.62
      pick: 0.0
      fit: 0.75
    The Reaper:
      total: 0.64
      efficiency: 0.5
      win: 0.89
      pick: 0.2
      fit: 0.35
    Pendulum Blade:
      total: 0.58
      efficiency: 0.42
      win: 0.65
      pick: 0.27
      fit: 0.85
    Arondight:
      total: 0.55
      efficiency: 0.5
      win: 0.62
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Pendulum Blade
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - The Crusher
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
    Underrated for this god: Hydra''s Lament, Tekko-Kagi, Tyrfing, Arondight, Runeforged
    Hammer, Avenging Blade, Golden Blade, Silverbranch Bow, Lernaean Bow, Shield Splitter,
    Dominance, Riptalon, Oath-Sworn Spear, Toxic Blade, Bloodforge, Deathbringer,
    Eye of the Storm, Damaru, Rage, Musashi''s Dual Swords, Sanguine Lash.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.71
      efficiency: 0.72
      win: 0.6
      pick: 0.69
      fit: 1.0
    The Reaper:
      total: 0.72
      efficiency: 0.5
      win: 0.89
      pick: 0.2
      fit: 0.91
    Pendulum Blade:
      total: 0.6
      efficiency: 0.42
      win: 0.65
      pick: 0.27
      fit: 1.0
    The Crusher:
      total: 0.49
      efficiency: 0.47
      win: 0.36
      pick: 0.28
      fit: 1.0
    Heartseeker:
      total: 0.6
      efficiency: 0.47
      win: 0.57
      pick: 0.63
      fit: 1.0
    Titan's Bane:
      total: 0.52
      efficiency: 0.47
      win: 0.42
      pick: 0.35
      fit: 1.0
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: *id001
---
