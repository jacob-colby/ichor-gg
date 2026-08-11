---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.6
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.49
    win_rate: 0.56
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.3
      win_rate: 0.58
    - name: Stampede
      pick_rate: 0.03
      win_rate: 0.45
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.56
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.2
      win_rate: 0.64
    - name: Breastplate of Valor
      pick_rate: 0.18
      win_rate: 0.55
  - name: Breastplate of Valor
    pick_rate: 0.18
    win_rate: 0.62
    alternates:
    - name: Genji's Guard
      pick_rate: 0.25
      win_rate: 0.51
    - name: Gladiator's Shield
      pick_rate: 0.07
      win_rate: 0.57
  - name: Dwarven Plate
    pick_rate: 0.1
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.62
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.55
  - name: Kinetic Cuirass
    pick_rate: 0.07
    win_rate: 0.52
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.56
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.56
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.59
    alternates:
    - name: Medal of Defense
      pick_rate: 0.05
      win_rate: 0.55
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.52
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.39
    win_rate: 0.52
  - name: Bumba's Hammer
    pick_rate: 0.34
    win_rate: 0.65
  - name: Bluestone Pendant
    pick_rate: 0.07
    win_rate: 0.47
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-08-10'
  god_win_rate: 0.5649819494584838
  god_matches_won: 626
  god_matches_played: 1108
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Gluttonous Grimoire, Jotunn''s Revenge,
    Freya''s Tears, The Crusher, Oni Hunter''s Garb, Shield Splitter, Shield of the
    Phoenix, Erosion, Hydra''s Lament, Eye of Providence, Eye of the Storm, Draconic
    Scale, Spectral Armor, Pharaoh''s Curse, Soul Gem, Leviathan''s Hide, Golden Blade,
    Mantle Of Discord, Stone of Binding, Midgardian Mail, Death Metal, Helm of Radiance,
    Avenging Blade, Shogun''s Ofuda, Magi''s Cloak, Lernaean Bow, Damaru, Ancile,
    Screeching Gargoyle, Yogi''s Necklace, Void Shield, Xibalban Effigy.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.56
      pick: 0.26
      fit: 0.31
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.37
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.66
      win: 0.62
      pick: 0.28
      fit: 0.31
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.52
      pick: 0.15
      fit: 0.67
    Shifter's Shield:
      total: 0.54
      efficiency: 0.52
      win: 0.56
      pick: 0.49
      fit: 0.57
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.57
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Shield of the Phoenix
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Soul Gem, Berserker''s Shield,
    Gluttonous Grimoire, Jotunn''s Revenge, Rod of Asclepius, Chandra''s Grace, The
    Crusher, Oni Hunter''s Garb, Freya''s Tears, Hydra''s Lament, Eye of the Storm,
    The Reaper, Shield Splitter, Erosion, Phoenix Feather, Eye of Providence, Spectral
    Armor, Pharaoh''s Curse, Draconic Scale, Blood-Bound Book, Bancroft''s Talon,
    Golden Blade, Leviathan''s Hide, Riptalon, Avenging Blade, Lifebinder, Midgardian
    Mail, Death Metal, Shogun''s Ofuda, Glorious Pridwen, Yogi''s Necklace, Lernaean
    Bow, Damaru.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.56
      pick: 0.26
      fit: 0.28
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.38
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.66
      win: 0.62
      pick: 0.28
      fit: 0.28
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.8
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.55
      win: 0.58
      pick: 0.3
      fit: 0.54
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Amanita Charm,
    Soul Gem, Berserker''s Shield, Stone of Binding, Avenging Blade, Screeching Gargoyle,
    Freya''s Tears, Void Shield, Spear of the Magus, Oni Hunter''s Garb, The Cosmic
    Horror, Void Stone, Hydra''s Lament, Shield of the Phoenix, The Reaper, Shield
    Splitter, Spear of Desolation, Erosion, Spectral Armor, Riptalon, Eye of Providence,
    Obsidian Shard, Eye of the Storm, Pharaoh''s Curse, Heartseeker, Draconic Scale,
    Silverbranch Bow, Leviathan''s Hide, Death Metal, Golden Blade, Helm of Radiance,
    Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.56
      pick: 0.26
      fit: 0.23
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.27
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.62
      pick: 0.28
      fit: 0.23
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.54
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.56
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
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
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Gluttonous Grimoire, Amanita Charm, Golden Blade,
    Pharaoh''s Curse, Jotunn''s Revenge, Riptalon, The Crusher, Freya''s Tears, Oni
    Hunter''s Garb, Soul Gem, Shogun''s Ofuda, Lernaean Bow, Shield of the Phoenix,
    Silverbranch Bow, Hydra''s Lament, Tyrfing, Spectral Armor, Erosion, Shield Splitter,
    Eye of Providence, Bracer of The Abyss, Draconic Scale, Eye of the Storm, Helm
    of Radiance, Leviathan''s Hide, Midgardian Mail, Mantle Of Discord, Yogi''s Necklace,
    Stone of Binding, Eros'' Bow, Death Metal, Dominance, Spear of the Magus, Rod
    of Asclepius.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.56
      pick: 0.26
      fit: 0.2
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.62
      pick: 0.28
      fit: 0.2
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
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Shield of the Phoenix
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Jotunn''s Revenge,
    Shield of the Phoenix, Soul Gem, Amanita Charm, Gluttonous Grimoire, Berserker''s
    Shield, Hydra''s Lament, Oni Hunter''s Garb, Gladiator''s Shield, Screeching Gargoyle,
    Chronos'' Pendant, The Crusher, Spear of Desolation, Chandra''s Grace, Erosion,
    Spectral Armor, Eye of Providence, Prophetic Cloak, Pharaoh''s Curse, Shield Splitter,
    Draconic Scale, Helm of Radiance, Gem of Focus, Leviathan''s Hide, Eye of the
    Storm, Mantle Of Discord, Midgardian Mail, Rod of Asclepius, Stone of Binding,
    Spear of the Magus, Death Metal, Arondight, Jade Scepter, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.56
      pick: 0.26
      fit: 0.48
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.29
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.66
      win: 0.62
      pick: 0.28
      fit: 0.48
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.46
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Gluttonous Grimoire
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield, Gluttonous
    Grimoire, The Crusher, Amanita Charm, Hydra''s Lament, Freya''s Tears, Soul Gem,
    Oni Hunter''s Garb, Shield Splitter, Pharaoh''s Curse, Golden Blade, Shield of
    the Phoenix, Lernaean Bow, Eye of the Storm, Erosion, Spectral Armor, Death Metal,
    Eye of Providence, Spear of the Magus, Shogun''s Ofuda, The Reaper, Draconic Scale,
    Damaru, Avenging Blade, The Cosmic Horror, Riptalon, Leviathan''s Hide, Helm of
    Radiance, Midgardian Mail, Mantle Of Discord, Stone of Binding, Heartseeker, Tekko-Kagi,
    Silverbranch Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.56
      pick: 0.26
      fit: 0.23
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.62
      pick: 0.28
      fit: 0.23
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.45
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
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge,
    The Crusher, Amanita Charm, Soul Gem, Berserker''s Shield, Freya''s Tears, Spear
    of the Magus, Oni Hunter''s Garb, Hydra''s Lament, Death Metal, The Cosmic Horror,
    Shield Splitter, Helm of Radiance, Shield of the Phoenix, Spear of Desolation,
    Erosion, Spectral Armor, Eye of the Storm, Rod of Asclepius, Eye of Providence,
    Pharaoh''s Curse, Obsidian Shard, Jade Scepter, Draconic Scale, Chronos'' Pendant,
    Golden Blade, Leviathan''s Hide, Blood-Bound Book, Lernaean Bow, The Reaper, Damaru,
    Bancroft''s Talon, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.56
      pick: 0.26
      fit: 0.23
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.27
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.62
      pick: 0.28
      fit: 0.23
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.41
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Berserker''s Shield, Gluttonous Grimoire,
    Jotunn''s Revenge, Freya''s Tears, The Crusher, Oni Hunter''s Garb, Shield Splitter,
    Shield of the Phoenix, Erosion, Hydra''s Lament, Eye of Providence, Eye of the
    Storm, Draconic Scale, Spectral Armor, Pharaoh''s Curse, Soul Gem, Leviathan''s
    Hide, Golden Blade, Mantle Of Discord, Stone of Binding, Midgardian Mail, Death
    Metal, Helm of Radiance, Avenging Blade, Shogun''s Ofuda, Magi''s Cloak, Lernaean
    Bow, Damaru, Ancile, Screeching Gargoyle, Yogi''s Necklace, Void Shield, Xibalban
    Effigy.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.56
      pick: 0.26
      fit: 0.31
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.52
      pick: 0.15
      fit: 0.67
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.57
  starter: *id001
---
