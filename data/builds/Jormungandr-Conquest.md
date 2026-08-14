---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unyielding
  aspect_pick_rate: 0.17
  aspect_win_rate: 0.67
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.33
    win_rate: 0.56
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.16
      win_rate: 0.71
    - name: Eye of Erebus
      pick_rate: 0.13
      win_rate: 0.5
  - name: Prophetic Cloak
    pick_rate: 0.15
    win_rate: 0.5
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.13
      win_rate: 0.43
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.5
  - name: Ethereal Staff
    pick_rate: 0.14
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.57
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.6
  - name: Gladiator's Shield
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.15
      win_rate: 0.67
    - name: Soul Reaver
      pick_rate: 0.13
      win_rate: 0.46
  - name: Hide of the Nemean Lion
    pick_rate: 0.09
    win_rate: 0.38
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.57
    - name: Soul Reaver
      pick_rate: 0.06
      win_rate: 0.33
  - name: Soul Reliquary
    pick_rate: 0.07
    win_rate: 0.75
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 1.0
    - name: Ethereal Staff
      pick_rate: 0.05
      win_rate: 0.67
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.38
    win_rate: 0.46
  - name: Bluestone Pendant
    pick_rate: 0.26
    win_rate: 0.57
  - name: Heroism
    pick_rate: 0.09
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-08-14'
  god_win_rate: 0.5462962962962963
  god_matches_won: 59
  god_matches_played: 108
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Jotunn's Revenge
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire,
    Jotunn''s Revenge, Pharaoh''s Curse, Freya''s Tears, Breastplate of Valor, The
    Crusher, Oni Hunter''s Garb, Golden Blade, Shield of the Phoenix, Shield Splitter,
    Hydra''s Lament, Lernaean Bow, Shogun''s Ofuda, Runeforged Hammer, Erosion, Eye
    of Providence, Spectral Armor, Eye of the Storm, Soul Gem, Draconic Scale, Leviathan''s
    Hide, Death Metal, Mantle Of Discord, Helm of Radiance, Midgardian Mail, Stone
    of Binding, Damaru, Bracer of The Abyss, Avenging Blade, Dominance, Riptalon,
    Yogi''s Necklace, Tyrfing, Bragi''s Harp, Magi''s Cloak, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.22
      fit: 0.26
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.48
    Pharaoh's Curse:
      total: 0.52
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.48
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Soul Gem,
    Kinetic Cuirass, Gluttonous Grimoire, Jotunn''s Revenge, Rod of Asclepius, Riptalon,
    Pharaoh''s Curse, The Crusher, Golden Blade, Chandra''s Grace, Breastplate of
    Valor, Oni Hunter''s Garb, Freya''s Tears, Runeforged Hammer, The Reaper, Hydra''s
    Lament, Shogun''s Ofuda, Lernaean Bow, Blood-Bound Book, Bancroft''s Talon, Phoenix
    Feather, Eye of the Storm, Spectral Armor, Erosion, Shield Splitter, Eye of Providence,
    Draconic Scale, Lifebinder, Leviathan''s Hide, Death Metal, Midgardian Mail, Avenging
    Blade, Yogi''s Necklace, Damaru, Helm of Radiance, Bracer of The Abyss.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.22
      fit: 0.23
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.49
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.32
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.56
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.76
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Berserker''s
    Shield, Kinetic Cuirass, Soul Gem, Amanita Charm, Stone of Binding, Avenging Blade,
    Screeching Gargoyle, Breastplate of Valor, Void Shield, Freya''s Tears, Spear
    of the Magus, Riptalon, Pharaoh''s Curse, Oni Hunter''s Garb, The Cosmic Horror,
    Silverbranch Bow, Hydra''s Lament, Void Stone, Golden Blade, Shield of the Phoenix,
    Lernaean Bow, Runeforged Hammer, The Reaper, Shield Splitter, Shogun''s Ofuda,
    Spectral Armor, Spear of Desolation, Erosion, Tekko-Kagi, Obsidian Shard, Eye
    of Providence, Eye of the Storm, Heartseeker, Draconic Scale, Death Metal, Helm
    of Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.22
      fit: 0.2
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.5
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Golden Blade, Pharaoh''s Curse, Breastplate of Valor, Jotunn''s Revenge, Riptalon,
    The Crusher, Freya''s Tears, Oni Hunter''s Garb, Soul Gem, Lernaean Bow, Shogun''s
    Ofuda, Shield of the Phoenix, Silverbranch Bow, Hydra''s Lament, Tyrfing, Runeforged
    Hammer, Spectral Armor, Erosion, Shield Splitter, Eye of Providence, Bracer of
    The Abyss, Draconic Scale, Helm of Radiance, Eye of the Storm, Leviathan''s Hide,
    Midgardian Mail, Mantle Of Discord, Yogi''s Necklace, Death Metal, Stone of Binding,
    Eros'' Bow, Dominance, Spear of the Magus, Damaru, Rod of Asclepius.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.22
      fit: 0.2
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.34
    Pharaoh's Curse:
      total: 0.52
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Berserker''s Shield, Breastplate of
    Valor, Freya''s Tears, Jotunn''s Revenge, Kinetic Cuirass, Gluttonous Grimoire,
    Soul Gem, Amanita Charm, Shield of the Phoenix, Hydra''s Lament, Pharaoh''s Curse,
    Oni Hunter''s Garb, The Crusher, Chronos'' Pendant, Screeching Gargoyle, Spear
    of Desolation, Shogun''s Ofuda, Chandra''s Grace, Spectral Armor, Erosion, Golden
    Blade, Lernaean Bow, Runeforged Hammer, Eye of Providence, Helm of Radiance, Shield
    Splitter, Draconic Scale, Gem of Focus, Bracer of The Abyss, Leviathan''s Hide,
    Spear of the Magus, Rod of Asclepius, Totem of Death, Death Metal, Eye of the
    Storm, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.57
      pick: 0.22
      fit: 0.41
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.39
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield, Gluttonous
    Grimoire, The Crusher, Kinetic Cuirass, Amanita Charm, Breastplate of Valor, Hydra''s
    Lament, Freya''s Tears, Soul Gem, Oni Hunter''s Garb, Runeforged Hammer, Shield
    Splitter, Pharaoh''s Curse, Golden Blade, Shield of the Phoenix, Lernaean Bow,
    Eye of the Storm, Erosion, Spectral Armor, Death Metal, Eye of Providence, Spear
    of the Magus, Shogun''s Ofuda, Damaru, Draconic Scale, The Reaper, The Cosmic
    Horror, Avenging Blade, Riptalon, Leviathan''s Hide, Helm of Radiance, Midgardian
    Mail, Mantle Of Discord, Stone of Binding, Heartseeker, Silverbranch Bow, Tekko-Kagi,
    Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.22
      fit: 0.23
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.52
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.41
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Berserker''s
    Shield, Jotunn''s Revenge, The Crusher, Kinetic Cuirass, Amanita Charm, Soul Gem,
    Breastplate of Valor, Freya''s Tears, Pharaoh''s Curse, Oni Hunter''s Garb, Spear
    of the Magus, Hydra''s Lament, Death Metal, The Cosmic Horror, Golden Blade, Lernaean
    Bow, Runeforged Hammer, Helm of Radiance, Shield of the Phoenix, Shield Splitter,
    Bracer of The Abyss, Spectral Armor, Shogun''s Ofuda, Rod of Asclepius, Spear
    of Desolation, Erosion, Riptalon, Eye of the Storm, Bragi''s Harp, Jade Scepter,
    Obsidian Shard, Eye of Providence, Chronos'' Pendant, Silverbranch Bow, Draconic
    Scale, Blood-Bound Book, Damaru, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.22
      fit: 0.2
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.46
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.49
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Jotunn's Revenge
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Kinetic Cuirass, Amanita Charm,
    Gluttonous Grimoire, Jotunn''s Revenge, Pharaoh''s Curse, Freya''s Tears, Breastplate
    of Valor, The Crusher, Oni Hunter''s Garb, Golden Blade, Shield of the Phoenix,
    Shield Splitter, Hydra''s Lament, Lernaean Bow, Shogun''s Ofuda, Runeforged Hammer,
    Erosion, Eye of Providence, Spectral Armor, Eye of the Storm, Soul Gem, Draconic
    Scale, Leviathan''s Hide, Death Metal, Mantle Of Discord, Helm of Radiance, Midgardian
    Mail, Stone of Binding, Damaru, Bracer of The Abyss, Avenging Blade, Dominance,
    Riptalon, Yogi''s Necklace, Tyrfing, Bragi''s Harp, Magi''s Cloak, Screeching
    Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.22
      fit: 0.26
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.48
    Pharaoh's Curse:
      total: 0.52
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.48
  starter: *id001
---
