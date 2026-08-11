---
type: smite-build
god: Tsukuyomi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Mangetsu
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.24
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.45
    win_rate: 0.56
    alternates:
    - name: Transcendence
      pick_rate: 0.21
      win_rate: 0.57
    - name: Hydra's Lament
      pick_rate: 0.11
      win_rate: 0.54
  - name: Transcendence
    pick_rate: 0.23
    win_rate: 0.53
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.15
      win_rate: 0.53
    - name: Jotunn's Revenge
      pick_rate: 0.13
      win_rate: 0.6
  - name: Hydra's Lament
    pick_rate: 0.15
    win_rate: 0.58
    alternates:
    - name: Heartseeker
      pick_rate: 0.12
      win_rate: 0.52
    - name: The Reaper
      pick_rate: 0.1
      win_rate: 0.65
  - name: Heartseeker
    pick_rate: 0.21
    win_rate: 0.53
    alternates:
    - name: Titan's Bane
      pick_rate: 0.11
      win_rate: 0.58
    - name: Hydra's Lament
      pick_rate: 0.08
      win_rate: 0.66
  - name: Titan's Bane
    pick_rate: 0.16
    win_rate: 0.56
    alternates:
    - name: Heartseeker
      pick_rate: 0.19
      win_rate: 0.64
    - name: Lucerne Hammer
      pick_rate: 0.05
      win_rate: 0.64
  - name: Blinking Abyss
    pick_rate: 0.07
    win_rate: 0.55
    alternates:
    - name: Heartseeker
      pick_rate: 0.06
      win_rate: 0.68
    - name: Lucerne Hammer
      pick_rate: 0.06
      win_rate: 0.63
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.37
    win_rate: 0.62
  - name: Bumba's Cudgel
    pick_rate: 0.24
    win_rate: 0.51
  - name: Archmage's Gem
    pick_rate: 0.11
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/tsukuyomi/
  last_verified: '2026-08-10'
  god_win_rate: 0.5575065847234416
  god_matches_won: 635
  god_matches_played: 1139
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - The Reaper
  - The Crusher
  flex_slots:
  - Death Metal
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Gluttonous Grimoire, Death Metal, Lernaean Bow, Berserker''s
    Shield, Damaru, Soul Gem, Riptalon, Golden Blade, Tekko-Kagi, Silverbranch Bow,
    Genji''s Guard, Bragi''s Harp, Dominance, Spear of the Magus, Tyrfing, Runeforged
    Hammer, Bracer of The Abyss, The Cosmic Horror, Breastplate of Valor, Pharaoh''s
    Curse, Demon Blade, Spear of Desolation, Obsidian Shard, Kinetic Cuirass, Amanita
    Charm, Shogun''s Ofuda, Avenging Blade, Oni Hunter''s Garb, Musashi''s Dual Swords,
    Shield Splitter, Nimble Ring, Pendulum Blade, Eye of Providence, Eros'' Bow.'
  slot_scores:
    Lernaean Bow:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.59
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.56
      pick: 0.45
      fit: 0.49
    Hydra's Lament:
      total: 0.53
      efficiency: 0.58
      win: 0.58
      pick: 0.23
      fit: 0.39
    Death Metal:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.51
    The Reaper:
      total: 0.55
      efficiency: 0.52
      win: 0.65
      pick: 0.16
      fit: 0.44
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - The Reaper
  - The Crusher
  flex_slots:
  - Death Metal
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Soul Gem, The Crusher, Death Metal, Genji''s Guard,
    Spear of the Magus, Spear of Desolation, The Cosmic Horror, Berserker''s Shield,
    Riptalon, Breastplate of Valor, Lernaean Bow, Obsidian Shard, Silverbranch Bow,
    Damaru, Bracer of The Abyss, Chronos'' Pendant, Bragi''s Harp, Tekko-Kagi, Golden
    Blade, Runeforged Hammer, Doom Orb, The World Stone, Freya''s Tears, Dreamer''s
    Idol, Pendulum Blade, Blood-Bound Book, Helm of Radiance, Bancroft''s Talon, Dominance,
    Gem of Focus, Pharaoh''s Curse, Tyrfing, Kinetic Cuirass, Shield of the Phoenix,
    Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.16
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.56
      pick: 0.45
      fit: 0.56
    Hydra's Lament:
      total: 0.54
      efficiency: 0.58
      win: 0.58
      pick: 0.23
      fit: 0.42
    Death Metal:
      total: 0.5
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.44
    The Reaper:
      total: 0.54
      efficiency: 0.52
      win: 0.65
      pick: 0.16
      fit: 0.4
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Soul Gem, Gluttonous Grimoire, Shield
    of the Phoenix, Kinetic Cuirass, Riptalon, The Crusher, Rod of Asclepius, Genji''s
    Guard, Pharaoh''s Curse, Oni Hunter''s Garb, Golden Blade, Blood-Bound Book, Chandra''s
    Grace, Bancroft''s Talon, Runeforged Hammer, Breastplate of Valor, Death Metal,
    Lernaean Bow, Shogun''s Ofuda, Phoenix Feather, Freya''s Tears, Damaru, Spectral
    Armor, Shifter''s Shield, Erosion, Eye of the Storm, Shield Splitter, Eye of Providence,
    Lifebinder, Spear of the Magus, Draconic Scale, Leviathan''s Hide, Silverbranch
    Bow, Yogi''s Necklace, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.45
      fit: 0.3
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.49
    Hydra's Lament:
      total: 0.52
      efficiency: 0.58
      win: 0.58
      pick: 0.23
      fit: 0.27
    The Reaper:
      total: 0.57
      efficiency: 0.52
      win: 0.65
      pick: 0.16
      fit: 0.57
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: anti-tank
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
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    for this god: The Crusher, Gluttonous Grimoire, Soul Gem, Riptalon, Spear of the
    Magus, Silverbranch Bow, Tekko-Kagi, The Cosmic Horror, Berserker''s Shield, Death
    Metal, Lernaean Bow, Avenging Blade, Damaru, Obsidian Shard, Spear of Desolation,
    Genji''s Guard, Golden Blade, Screeching Gargoyle, Runeforged Hammer, Doom Orb,
    The World Stone, Breastplate of Valor, Pendulum Blade, Dominance, Dreamer''s Idol,
    Bragi''s Harp, Bracer of The Abyss, Toxic Blade, Tyrfing, Pharaoh''s Curse, Stone
    of Binding, Kinetic Cuirass, Void Shield, Amanita Charm, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.56
      pick: 0.45
      fit: 0.6
    Hydra's Lament:
      total: 0.52
      efficiency: 0.58
      win: 0.58
      pick: 0.23
      fit: 0.32
    The Reaper:
      total: 0.57
      efficiency: 0.52
      win: 0.65
      pick: 0.16
      fit: 0.57
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.67
    Heartseeker:
      total: 0.51
      efficiency: 0.45
      win: 0.53
      pick: 0.35
      fit: 0.67
    Titan's Bane:
      total: 0.51
      efficiency: 0.45
      win: 0.56
      pick: 0.35
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Berserker's Shield
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Gluttonous Grimoire, Berserker''s Shield, The Crusher, Silverbranch
    Bow, Golden Blade, Soul Gem, Lernaean Bow, Tyrfing, Death Metal, Genji''s Guard,
    Damaru, Bracer of The Abyss, Pharaoh''s Curse, Spear of the Magus, Tekko-Kagi,
    Dominance, Breastplate of Valor, Bragi''s Harp, Toxic Blade, The Cosmic Horror,
    Runeforged Hammer, Nimble Ring, Blood-Bound Book, Kinetic Cuirass, Shogun''s Ofuda,
    Bancroft''s Talon, Amanita Charm, Oni Hunter''s Garb, Obsidian Shard, Eye of Providence,
    Eros'' Bow, Spear of Desolation, Demon Blade, Freya''s Tears, Helm of Radiance.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.45
      fit: 0.3
    Hydra's Lament:
      total: 0.52
      efficiency: 0.58
      win: 0.58
      pick: 0.23
      fit: 0.27
    The Reaper:
      total: 0.54
      efficiency: 0.52
      win: 0.65
      pick: 0.16
      fit: 0.36
    Riptalon:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.65
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Genji''s Guard, Breastplate
    of Valor, Gluttonous Grimoire, The Crusher, Spear of Desolation, Berserker''s
    Shield, Chronos'' Pendant, Freya''s Tears, Death Metal, Shield of the Phoenix,
    Spear of the Magus, Lernaean Bow, Gem of Focus, Riptalon, Damaru, The Cosmic Horror,
    Bracer of The Abyss, Screeching Gargoyle, Silverbranch Bow, Chandra''s Grace,
    Arondight, Pendulum Blade, Golden Blade, Bragi''s Harp, Obsidian Shard, Pharaoh''s
    Curse, Runeforged Hammer, Kinetic Cuirass, Amanita Charm, Blood-Bound Book, Tekko-Kagi,
    Oni Hunter''s Garb, Dominance, Helm of Radiance, Bancroft''s Talon, Tyrfing.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.56
      pick: 0.45
      fit: 0.59
    Hydra's Lament:
      total: 0.56
      efficiency: 0.58
      win: 0.58
      pick: 0.23
      fit: 0.55
    The Crusher:
      total: 0.5
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.34
    Soul Gem:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - Gluttonous Grimoire
  - Spear of the Magus
  - The Crusher
  flex_slots:
  - The Crusher
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Gluttonous Grimoire, Soul Gem, Death Metal,
    The Crusher, Spear of the Magus, Genji''s Guard, The Cosmic Horror, Spear of Desolation,
    Berserker''s Shield, Bracer of The Abyss, Bragi''s Harp, Lernaean Bow, Chronos''
    Pendant, Obsidian Shard, Breastplate of Valor, Damaru, Riptalon, Blood-Bound Book,
    Helm of Radiance, Bancroft''s Talon, Silverbranch Bow, Golden Blade, Rod of Asclepius,
    Gem of Focus, Doom Orb, The World Stone, Runeforged Hammer, Nimble Ring, Jade
    Scepter, Tekko-Kagi, Dreamer''s Idol, Dominance, Ancient Signet, Freya''s Tears,
    Pharaoh''s Curse, Tyrfing, Kinetic Cuirass.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.56
      pick: 0.45
      fit: 0.46
    Hydra's Lament:
      total: 0.53
      efficiency: 0.58
      win: 0.58
      pick: 0.23
      fit: 0.39
    Death Metal:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.54
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.51
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.41
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - The Reaper
  - Spear of the Magus
  - The Crusher
  flex_slots:
  - Death Metal
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, The Crusher,
    Death Metal, Soul Gem, Spear of the Magus, Berserker''s Shield, Lernaean Bow,
    The Cosmic Horror, Bragi''s Harp, Damaru, Bracer of The Abyss, Genji''s Guard,
    Riptalon, Obsidian Shard, Golden Blade, Spear of Desolation, Tekko-Kagi, Silverbranch
    Bow, Runeforged Hammer, Dominance, Blood-Bound Book, Tyrfing, Helm of Radiance,
    Breastplate of Valor, Bancroft''s Talon, Chronos'' Pendant, Doom Orb, The World
    Stone, Rod of Asclepius, Nimble Ring, Dreamer''s Idol, Jade Scepter, Pharaoh''s
    Curse, Triton''s Conch, Kinetic Cuirass, Ancient Signet.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.56
      pick: 0.45
      fit: 0.44
    Hydra's Lament:
      total: 0.53
      efficiency: 0.58
      win: 0.58
      pick: 0.23
      fit: 0.36
    Death Metal:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.59
    The Reaper:
      total: 0.54
      efficiency: 0.52
      win: 0.65
      pick: 0.16
      fit: 0.41
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.41
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.51
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Lernaean Bow
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Gluttonous Grimoire, Death Metal, Lernaean
    Bow, Berserker''s Shield, Damaru, Soul Gem, Riptalon, Golden Blade, Tekko-Kagi,
    Silverbranch Bow, Genji''s Guard, Bragi''s Harp, Dominance, Spear of the Magus,
    Tyrfing, Runeforged Hammer, Bracer of The Abyss, The Cosmic Horror, Breastplate
    of Valor, Pharaoh''s Curse, Demon Blade, Spear of Desolation, Obsidian Shard,
    Kinetic Cuirass, Amanita Charm, Shogun''s Ofuda, Avenging Blade, Oni Hunter''s
    Garb, Musashi''s Dual Swords, Shield Splitter, Nimble Ring, Pendulum Blade, Eye
    of Providence, Eros'' Bow.'
  slot_scores:
    Lernaean Bow:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.56
      pick: 0.45
      fit: 0.49
    Death Metal:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.37
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: *id001
---
